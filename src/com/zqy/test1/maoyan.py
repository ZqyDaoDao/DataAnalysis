import requests
import pandas as pd
import numpy as np
from pyecharts import Pie
from pyecharts import Bar

base_url = "http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset="


#爬取每一页评论
def crawl_one_page_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"
    }

    response = requests.get(url, headers=headers)

    #页面访问不成功
    if response.status_code != 200:
        return []

    return response.json()

#解析每一个获得的结果
def parse(data):
    result = []

    # 影评数据在 cmts 这个 key 中

    comments = data.get("cmts")

    if not comments:
        return []

    for cm in comments:
        yield [
            cm.get("id"),  # 影评id
            cm.get("time"),  # 影评时间
            cm.get("score"),  # 影评得分
            cm.get("cityName"),  # 影评城市
            cm.get("nickName"),  # 影评人
            cm.get("gender"),  # 影评人性别，1 表示男性，2表示女性
            cm.get("content") # 影评内容
        ]

#爬取影评
def crawl_film_review(total_page_num=100):
    data = []
    for i in range(1, total_page_num + 1):
        print("抓取数据" + str(i))
        url = base_url + str(i)
        crawl_data = crawl_one_page_data(url)
        if crawl_data:
            data.extend(parse(crawl_data))
    return data



if __name__ == '__main__':

    # columns = ["id", "time", "score", "city", "nickname", "gender", "content"]
    # df = pd.DataFrame(crawl_film_review(4000), columns=columns)
    # # 将性别映射后的数字转为汉字
    # df["gender"] = np.where(df.gender==1, "男性", "女性")
    # # 根据id去除重复影评
    # df=df.drop_duplicates(subset=["id"])
    # print("执行到这里了1")
    #
    # # 保存抓取数据，方便后续使用。
    # df.to_csv("《一出好戏》影评_1000.csv", index=False)
    df = pd.read_csv("《一出好戏》影评_1000.csv", encoding="utf-8")



    # # 求出不同性别出现的次数
    # gender_count = df.gender.value_counts().to_dict()
    # # 性别分析
    # pie = Pie("性别分析")
    # pie.add(name="", attr=gender_count.keys(), value=gender_count.values(), is_label_show=True)
    # pie.show_config()
    # pie.render()

    # # 求出不同评分出现的次数
    # score_count = df.score.value_counts().sort_index()
    # score_list = score_count.index.tolist()
    # count_list = score_count.tolist()
    #
    # bar = Bar("评分分布", width=450, height=450)
    # bar.add("", score_list, count_list)
    # bar.show_config()
    # bar.render()

    # # 求出不同性别评分的均值
    # sex_score_mean = df.groupby(["gender"])["score"].mean().to_dict()
    #
    # bar = Bar("不同性别评分的差异", width=450, height=450)
    # bar.add("", list(sex_score_mean.keys()), list(sex_score_mean.values()), is_stack=True)
    # bar.show_config()
    # bar.render()

    # # 求出不同城市评分的均值
    # city_list = ["北京", "上海", "西安", "太原"]
    # gender_city_score_mean = df[df.city.isin(city_list)].groupby(["gender", "city"], as_index=False)["score"].mean()
    # city_data, city_index = pd.factorize(gender_city_score_mean.city)
    # gender_data, gender_index = pd.factorize(gender_city_score_mean.gender)
    # data = list(zip(city_data, gender_data, gender_city_score_mean.score.values))
    #
    # from pyecharts import Bar3D
    # bar3d = Bar3D("一线城市与二线城市的评分差异", width=650, height=450)
    # range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    #                '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    # bar3d.add("", city_index, gender_index, data,
    #           is_visualmap=True, visual_range=[0, 5],
    #           visual_range_color=range_color, grid3d_width=150, grid3d_depth=80, is_grid3d_rotate=False)
    # bar3d.show_config()
    # bar3d.render()

#     影评词云图
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import jieba
    import matplotlib.pyplot as plt
    # 将分词后的结果以空格连接
    words = " ".join(jieba.cut(df.content.str.cat(sep=" ")))
    # 导入背景图
    backgroud_image = plt.imread("黄渤.jpg")

    #设置停用词
    stopwords = STOPWORDS
    stopwords.add("电影")

    wc = WordCloud(stopwords=stopwords,
                   mask=backgroud_image, background_color="white", max_words=100)
    my_wc = wc.generate_from_text(words)

    ImageColorGenerator

    image_colors = ImageColorGenerator(backgroud_image)

    plt.imshow(my_wc)
    # plt.imshow(my_wc.recolor(color_func=image_colors), )
    plt.axis("off")
    plt.show()






