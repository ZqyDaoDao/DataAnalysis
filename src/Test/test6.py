import pandas as pd
import requests
import time
from lxml import html
from collections import defaultdict, Counter
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"] #用来正常显示中文标签
plt.rcParams["axes.unicode_minus"]=False #用来正常显示负号

if __name__ == '__main__':

    data = defaultdict(list)

    for i in range(10):
        url = "https://movie.douban.com/top250?start={}&filter=".format(i*25)
        print("正在抓取：{}".format(url))

        content = requests.get(url).content
        sel = html.fromstring(content)


        # 我们需要提取的信息都在class属性为info的div标签里
        for single_movie_info in sel.xpath('//div[@class="info"]'):
            # 电影名称
            title = single_movie_info.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]

            # 包含了除名称之外的其他信息
            info = single_movie_info.xpath('div[@class="bd"]')[0]

            # 导演和主演
            director_and_performer = info.xpath('p[1]/text()')[0].strip()

            # 时间、地点、类型
            year_and_place_and_genre = info.xpath('p[1]/text()')[1].strip().split("/")
            # 时间
            year = year_and_place_and_genre[0].strip()
            # 地点
            place = year_and_place_and_genre[1].strip()
            # 类型
            genre = year_and_place_and_genre[2].strip()

            # 评分
            rating = info.xpath('div/span[@class="rating_num"]/text()')[0]
            # 评论用户数
            rating_num = info.xpath('div/span[last()]/text()')[0].split("人评价")[0]

            data["title"].append(title)
            data["director_and_performer"].append(director_and_performer)
            data["year"].append(year)
            data["place"].append(place)
            data["genre"].append(genre)
            data["rating"].append(rating)
            data["rating_num"].append(rating_num)

        time.sleep(1)

    df = pd.DataFrame(data)

    df["year"] = pd.to_numeric(df.year.str.replace("\(.*?\)", ""))
    df["rating"] = pd.to_numeric(df.rating)
    df["rating_num"] = pd.to_numeric(df.rating_num)

    year_sta = df.year.value_counts()
    year_sta[:10].plot.bar()
    plt.show()

    #先筛选出21世纪高评分的电影，然后进行统计。
    year_21century = df[df.year >= 2000].year.value_counts().sort_index()
    year_21century.plot.line()
    plt.show()

    #对所有的地区进行统计，由于有的电影会出现多个地区，所以需要分开统计。
    place = []
    print("-----------------------------------")
    print(df.place.str.split(" ").values)
    for i in df.place.str.split(" ").values:
        for j in i:
            place.append(j)
#     求出不同区域的次数
    place_count = Counter(place)
#     对结果进行排序
    place_count = sorted(place_count.items(), key=lambda item: item[-1], reverse=True)
#     将结果进行组装
    place_count = list(zip(*place_count))
    #构建Series
    place_count_series = pd.Series(data=place_count[1], index=place_count[0])

    place_count_series.plot.area()
    plt.show()

    place_count_series2 = place_count_series[:9]
    place_count_series2["其他"] = place_count_series[9:].sum()
    place_count_series2.plot.pie(figsize=(5, 5), autopct="%.2f")

    plt.show()


    #产出的高评分电影最多体裁Top10¶
    genre = []
    for i in df.genre.str.split(" ").values:
        for j in i:
            genre.append(j)
    # 求出不同体裁的次数
    genre_count = Counter(genre)
    # 对结果进行排序
    genre_count = sorted(genre_count.items(), key=lambda item: item[-1], reverse=True)
    # 将结果进行组装
    genre_count = list(zip(*genre_count))
    # 构建 Series
    genre_count_series = pd.Series(data=genre_count[1], index=genre_count[0])

    genre_count_series.plot.area()
    plt.show()

    #直接按照评分字段排序，获取前十即可。

    rating_top10 = df.sort_values(by="rating", ascending=False)[:10]
    rating_top10.plot.barh(x="title", y="rating")

    plt.show()

    # 评论人数最多电影Top10¶


    rating_num_top10 = df.sort_values(by="rating_num", ascending=False)[:10]
    rating_num_top10.plot.barh(x="title", y="rating_num")
    plt.show()

    # 评论人数与评分高低之间的关系¶

    df.plot.scatter(x="rating_num", y="rating")
    plt.show()

    # 实力派导演Top10¶
    director = df.director_and_performer.map(lambda x: x.split(":")[1].strip().split(" ")[0])
    director.value_counts()[:10].plot.barh()

    plt.show()

