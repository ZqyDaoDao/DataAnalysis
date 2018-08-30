import pandas as pd

# Pandas之数据导入、导出

# Pandas封装一些方法，用
# 于将不同格式的列表数据转换为DataFrame。同时也可以将DataFrame存为文件。
# 本文以读取csv文件和excel文件为例来说明下一些常用的方法。

# 数据导入

if __name__ == '__main__':
    data = pd.read_csv('data.csv')
    print(data.head())