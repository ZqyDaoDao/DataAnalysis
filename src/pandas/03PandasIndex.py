# pandas 的索引操作
import pandas as pd


if __name__ == '__main__':

    data = pd.read_excel('excel-comp-data.xlsx')
    print(data)

    data2 = pd.read_excel('excel-comp-data.xlsx', index_col='id')
    print(data2.head())

    new_index_col = data2.state.map(lambda x: x + '_') + data2.name
    data_new = data2.copy()
    data_new.index = new_index_col
    print(data_new.head())

    print(data_new.index.is_unique)

    # 2  索引处理
    # 有时候需要重建索引，常用的一个方法是reindex方法，可以用它来改变行顺序，列顺序。
    print('将行顺序进行反转')

    print(data.reindex(index = data.index[::-1]))

    print('# 将行顺序反转，列只取[''street'',''name'']两列')
    print(data.reindex(index=data.index[::-1], columns=['street', 'Jan']))

    # print("使用method可以按照特定的形式补齐NaN值，使用fill_value可以指定将NaN值指定为特定的值。")
    # print(data.reindex(index=data.index[::-1], method='ffill', columns=['Feb', 'Jan']))
    #
    # print(data.reindex(index=data.index[::-1], fill_value='1', columns=['street', 'Jan']))

    # new_index = data.index[::-1]
    # col = ['street', 'Jan']
    # print(data.ix[new_index, col])

    print("整理之前的数据: ")
    print(data)
    print("整理之后的数据: ")
    print(data.drop([1, 3]))


    print("使用 . 方式索引列出指定数据")
    print(data.city)