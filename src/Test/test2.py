import pandas as pd
import numpy as np

if __name__ == '__main__':
    try:
        data = pd.read_csv("./../../data/ml-latest-small/user_for_movie_ratings_summary.csv", encoding = "gbk")
        print(data.head())
        print(data.shape)
        print(data.head(2))
        print(data[:2])
        print(data.tail(2))
        print(data[4:9])
        print(data[::3].head())
        print(data.get("rating").head())
        print("通过属性的方式")
        print(data.rating.head())
        print("通过切片的方式")
        print(data["rating"].head())
        print("通过to_frame方法转化DataFrame")
        print(data.rating.to_frame().head())
        print("将切片传入一个列表")
        print(data[["rating"]].head())
        print("涮选某一列或者多列")
        clos = ["userId", "movieId", "rating"]
        print(data[clos].head())

        print("根据行涮选数据")
        print(data[:5]["rating"])

        print(data.loc[0:5, "rating"])

        print("2,   a表述索引为2")
        print(data.iloc[0:5, 2])

        print("-------------------------")
        print("根据布尔条件涮选")
        print(data[data["movieId"] == 2049])

        print(data[(data["movieId"] == 2049) | (data["movieId"] == 6268)])

        print("用isin 实现")
        mids = [2049, 6268]
        print(data[data["movieId"].isin(mids)])
    except Exception as e:
        print(e)

