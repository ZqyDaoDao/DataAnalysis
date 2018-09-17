import pandas as pd

# Pandas之数据导入、导出

# Pandas封装一些方法，用
# 于将不同格式的列表数据转换为DataFrame。同时也可以将DataFrame存为文件。
# 本文以读取csv文件和excel文件为例来说明下一些常用的方法。

# 数据导入

if __name__ == '__main__':
    data = pd.read_csv('data.csv', encoding='utf-8')
    print(data.head())

    print(pd.read_csv('data.csv', sep=',',header=None, names=['a','b','c','d'],encoding='utf-8').head())

    print(pd.read_csv('data.csv', sep=',', header=None, encoding='utf-8').head())

    print(pd.read_csv('data.csv', sep=',', encoding='utf-8', index_col=[u'频道', u'关键字', ]))

    # print(pd.read_csv('data.csv', sep=', ', encoding='utf-8', nrows=2))


#     2 读取excel文件

    # Pandas封装了read_excel方法用来读取excel文件。其中有一个sheetname参数，默认为0，代表读取sheet1，
    # 当然了，也可以将sheetname设为字符串，表示读取sheet的名字。
    print('read excel file')
    print(pd.read_excel('data.xlsx', sheet_name=0, sep=''))

    print('read excel name')
    print(pd.read_excel('data.xlsx', sheet_name='data'))

    print('export data')
    data.to_csv('test.csv', encoding='utf-8')

    # 将数据保存到磁盘的一个有效的存储方式是二进制，Pandas利用Python内建的pickle序列化来实现。
    print('data export disk')
    data.to_pickle('test_pickle')

    print('pickle print ')
    pd.read_pickle("test_pickle")





