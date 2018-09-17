import pandas as pd
import requests
import time
from collections import defaultdict


#用数据来说明数据分析岗位的竞争力


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=",
}

cookies = {
    "Cookie": "JSESSIONID=ABAAABAAADEAAFI3E2AE80419BA8FFB6F5FFB49D1573C34; _ga=GA1.2.260226169.1531815206; user_trace_token=20180717161326-47e61066-8999-11e8-9c54-525400f775ce; LGUID=20180717161326-47e613e7-8999-11e8-9c54-525400f775ce; _gid=GA1.2.1025242393.1534486196; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534486196; TG-TRACK-CODE=index_search; fromsite=translate.baiducontent.com; utm_source=""; index_location_city=%E5%8C%97%E4%BA%AC; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534650094; _gat=1; LGSID=20180819114134-c4f1bc52-a361-11e8-a9f8-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3Fcity%3D%25E5%258C%2597%25E4%25BA%25AC%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20180819114134-c4f1bf1a-a361-11e8-a9f8-5254005c3644; SEARCH_ID=c5acefc2c73649dea43d17ec5f57b810"
}


def crawl_lagou_data(city, kd, pn=1):
    url = "https://www.lagou.com/jobs/positionAjax.json?city={city}&needAddtionalResult=false".format(city=city)

    data = {
        "first": True,
        "pn": pn,
        "kd": kd
    }

    rp = requests.post(url, headers=headers, cookies=cookies, data=data)

    result = rp.json()
    if not result["success"]:
        print("pn: %s, 抓取失败" % pn)
        return []
    return result["content"]["positionResult"]["result"]

result = defaultdict(list)


def calculate_salary_mean(salary_str):
    salary_sum = 0
    salary_list = salary_str.upper().replace("K", "000").split("-")

    for i in salary_list:
        salary_sum += int(i)

    return salary_sum/len(salary_list)

if __name__ == '__main__':

    # for i in range(1, 50):
    #     print("正在抓取第 %s 页" % i, end="\r")
    #     job_infos = crawl_lagou_data("北京", "数据分析", i)
    #     for job_info in job_infos:
    #         result["positionId"].append(job_info.get("positionId"))
    #         result["city"].append(job_info.get("city"))
    #         result["companyLabelList"].append(",".join(job_info.get("companyLabelList")))
    #         result["companyShortName"].append(job_info.get("companyShortName"))
    #         result["companySize"].append(job_info.get("companySize"))
    #         result["district"].append(job_info.get("district"))
    #         result["education"].append(job_info.get("education"))
    #         result["salary"].append(job_info.get("salary"))
    #         result["workYear"].append(job_info.get("workYear"))
    #         result["financeStage"].append(job_info.get("financeStage"))
    #         result["subwaylin e"].append(job_info.get("subwayline"))
    #     print("抓取第 %s 页成功" % i, end="\r")
    #     time.sleep(10)
    # df = pd.DataFrame(result)
    #
    # print("去重前数据：{}".format(df.shape))
    # df = df.drop_duplicates(subset=["positionId"])
    # print("去重后的数据：{}".format(df.shape))
    #
    # df.to_csv('df.csv', index=False)

    df = pd.read_csv('df.csv')

    import matplotlib.pyplot as plt
    plt.rcParams["font.sans-serif"] = ["SimHei"] #用来正常显示中文标签
    plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号

    plt.title("招聘数据分析岗位最多的公司Top10")
    company_count = df.companyShortName.value_counts()[:10]  #在pandas里面常用用value_counts确认数据出现的频率。

    company_count.plot.bar()
    plt.show()

    print("什么样的学历能够胜任数据分析呢？")
    plt.title("招聘数据分析岗位对学历的要求")
    df.education.value_counts().plot.pie(figsize=(10, 10), autopct="%.2f")  #设置图框的大小fig = plt.figure(figsize=(10,6))
    plt.show()


    print("北京哪个区的数据分析岗位机会最多？")
    plt.title("北京不同区的数据分析岗位机会对")
    data = df.district.value_counts().plot.barh()
    plt.show()


    from pyecharts import Geo

    data = df.district.value_counts().to_dict()

    geo = Geo(
        "北京",
        "job",
        title_color="#fff",
        title_pos="center",
        width=600,
        height=400,
        background_color="#404a59"
    )

    attr, value = geo.cast(data)

    geo.add(
        "",
        attr,
        value,
        visual_range=[0, 150],
        maptype="北京",
        visual_text_color="#fff",
        symbol_size=15,
        is_visualmap=True,

    )
    print(geo)
    # geo.show()


    print("不同工作年限的数据分析师是什么收入水平？")
    #计算每条招聘信息中新增的平均年薪
    df["salary_mean"] = df["salary"].map(lambda x:calculate_salary_mean(x))

    plt.title("不同工作年限的数据分析岗位的薪资对比")
    work_year_salary_man = df.groupby("workYear")["salary_mean"].mean()
    work_year_salary_man.plot.bar()
    plt.show()
