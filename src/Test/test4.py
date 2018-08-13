import pandas as pd
import numpy as np

# %matplotlib inline

if __name__ == '__main__':

    tips = pd.read_csv("./../../data/tips.csv")
    print(tips.head())

    print("统计小费")
    grouped = tips.groupby("time")["tip"]
    print("不同时间的小费均值")
    print(grouped.mean())
    print("不同时间的小费方差")
    print(grouped.var())

    grouped = tips.groupby("sex")["total_bill", "tip"]

    print("将total_bill和tip根据不同的sex进行标准化¶")
    tips_standardization = grouped.transform(lambda arr: (arr - arr.mean())/arr.std())\
        .join(tips["sex"])

    print(tips_standardization.head())

    print("计算吸烟者和非吸烟者给出的小费比列值的均值")
    tips["tips_rating"] = tips.tip / tips.total_bill
    print(tips.groupby("smoker")["tips_rating"].mean())

    print("对time和size聚合得到均值，画出total_bill的饼图")
    tips.groupby(["time", "size"])["total_bill"].mean().plot(kind="pie", figsize=(6, 6), autopct="%.2f")
