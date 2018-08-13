import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

if __name__ == '__main__':
    movies = pd.read_csv("./../../data/ml-latest-small/movies.csv")
    print(movies.head(2))
    movies.dropna(subset=["genres"], inplace=True)

    print("标题转换为小写")
    print(movies.title.str.lower().head())

    print(movies.genres.map(lambda x: len(x.split("|"))).head())

    print("根据体裁生成多列数据")
    print(movies.genres.str.split("|", expand = True).head())

    print("替换分隔符")
    print(movies.genres.str.replace("|",",").head())

    print("提取上映年份")
    print(movies.title.str.extract("\((\d+)\)", expand=True).head())
    print("去除标题得年份")
    print(movies.title.str.replace("\(\d+\)", "").head())

    ts = movies.genres.str.cat(sep=" ")
    wc = WordCloud()
    my_wc = wc.generate_from_text(ts)
    plt.imshow(my_wc)
    plt.axis("off")
    plt.show()