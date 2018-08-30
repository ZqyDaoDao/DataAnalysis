import pandas as pd
import numpy as np

# Pandas 常用的数据结构就2中。一种是DataFramw, 另一种是Series。Series底层结构是numpy中的数组，不同的是Series有自己的索引，DataFrame是由多个Series构成的。

# Series
# 1.1 构造Series
if __name__ == '__main__':
    counts = pd.Series([12, 15, 8, 20])
    print(counts)
    print('index: \n', counts.index)
    print('value: \n', counts.values)

    # 自己指定index
    name_age = pd.Series(data=[12, 15, 8, 20], index=['tom','ken','kitty','jerry'])
    print(name_age)

    name_age_dict = {'tom': 12, 'ken': 15, 'kitty': 8, 'jerry': 20}
    name_age = pd.Series(data=name_age_dict,index=['tom','ken','kitty','xiaoming'])
    print(name_age)

#     1.2 访问Series 三种方式
    print(name_age.tom)
    print(name_age['tom'])
    print(name_age[0])

# 通过索引名称形式访问时，索引也可以是一个序列。下面的语句将得到name中所有以‘y’结尾的数据。
    print(name_age[[name.endswith('y') for name in name_age.index]])
    # 1.3 筛选Series
    # isnull()和notnul()方法可以判断是缺失值或不是缺失值
    print(name_age.isnull())
    # 通过以下两种方法可以去除掉缺失值。
    print(name_age[~name_age.isnull()])

    print(name_age[name_age.notnull()])

    # 通过Series中的值可以直接进行筛选，例如，得到所有年龄大于平均年龄的数据。
    print(name_age[name_age > np.mean(name_age)])

    print(name_age.index)

    print(name_age.values)

    print(name_age.value_counts())


    # 2. DataFrame
    # DataFrame 是一个表格型的数据结构，它含有一组有序的列（类似于 index），
    # 每列可以是不同的值类型（不像 ndarray 只能有一个 dtype）。
    # 基本上可以把 DataFrame 看成是共享同一个 index 的 Series 的集合。

    #2.1  构造DataFrame
    data = [['tom', 'ken', 'kitty', 'jerry'], [12, 15, 8, 20]]
    print(data)

    zip(*data)
    print("zip(data):")
    print(list(zip(data)))
    print("zip(*data):")
    print(list(zip(*data)))

    dates = pd.date_range(start='20160726', periods=4)
    print(dates)
    #DatetimeIndex(['2016-07-26', '2016-07-27', '2016-07-28', '2016-07-29'], dtype='datetime64[ns]', freq='D')

    # data = pd.DataFrame(data=zip(*data), index=dates, columns=['name', 'age'])
    # print(data.info())

    data = pd.DataFrame(data={'name': ['tom', 'ken', 'kitty', 'jerry'], 'age': [12, 15, 8, 20], }, index=dates,
                        columns=['name', 'age'])
    print(data)

    # 2.2
    # 访问DataFrame

    # 2.2.1
    # 访问列数据
    # DataFrame是按照列名分类的，我们可以通过属性（“.列名”）的方式来访问该列的数据，也可以通过[column名称]
    # 的形式来访问该列的数据。例如，想要得到name列，通过以下两种方式都可以得到。
    print(data.name)

    print(type(data.name))

    print(data[['age', 'name']])

    # 2.2.2 访问行数据
    # 访问数据可以通过ix,iloc,loc三种方式访问，
    # 区别见<a href = "http://blog.csdn.net/xw_classmate/article/details/51333646">Pandas——ix vs loc vs iloc 区别</a>
    # ，这里以ix为例来访问。
    print(data.ix[0:1])

    print(data.ix['2016-07-26':'2016-07-27'])  # 使用index名称访问

    # 2.2.3 访问特定行、列数据
    print(data.ix[0:3, [0, 1]])
    print(data.ix[0:2], ['age', 'name'])

    # 2.2.4访问数据时注意事项
    # 由DataFrame返回的Series引用并没有复制数据本身，也就是说对得到的Series数据的更改会改变原有DataFrame的数值。

    print(data.age)

    # 2.3为DataFrame增加数据
    data['region'] = 'A区'
    print(data)

    data['region'] = ['A区', 'C区', 'D区', 'B区']
    print(data)

    print(data.T)





