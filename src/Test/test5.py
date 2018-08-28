import itchat
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import _rebuild
_rebuild()

if __name__ == '__main__':
    # 执行后会弹出二维码，扫描验证，登陆
    itchat.auto_login(hotReload=True)

    # 登陆成功后，借助get_friends即可获取自己的好友信息
    friends = itchat.get_friends(update=True)
    # 获取信息后，我们将需要字段（NickName、Sex、Province、City、Signature）筛选出来，然后构建成一个DataFrame。
    friends_dict = defaultdict(list)
    for friend in friends:
        friends_dict["NickName"].append(friend["NickName"])
        friends_dict["Sex"].append(friend["Sex"])
        friends_dict["Province"].append(friend["Province"])
        friends_dict["City"].append(friend["City"])
        friends_dict["Signature"].append(friend["Signature"])
        friends_dict["RemarkName"].append(friend["RemarkName"])

    df = pd.DataFrame(friends_dict)
    print("好友信息：")
    print(df.shape)
    print(df.head(10))

    font_set = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc", size=12)

    #先来看看好友中的性别分布，需要注意的是，用户性别已经编码成数字了，经过验证，0表示未知、1表示男、2表示女。
    # % matplotlib inline
    df.groupby("Sex").size().plot.pie(figsize=(4, 4), autopct="%.2f")
    plt.show()

    # 这里我取出好友数最多的前20个省份来作图。
    plt.rcParams['font.sans-serif'] = [u'PingFang'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    df.Province.value_counts()[:20].plot.bar()
    plt.show()

    # 再来看下地区或城市的好友的分布。
    df.City.value_counts()[:20].plot.bar()
    plt.show()

    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import jieba
    import matplotlib.pyplot as plt

    signs = df.Signature.str.replace("<.*?>", "", )
    # 将分词后的结果以空格连接
    words = " ".join(jieba.cut(signs.str.cat(sep=" ")))
    # words = " ".join(jieba.cut(df.Signature.str.cat(sep=" ")))

    # 设置停用词
    stopwords = STOPWORDS

    wc = WordCloud(stopwords=stopwords,
                   font_path="/System/Library/Fonts/STHeiti Light.ttc",  # 解决显示口字型乱码问题
                   background_color="white", max_words=100)

    my_wc = wc.generate_from_text(words)

    plt.imshow(my_wc)
    # plt.imshow(my_wc.recolor(color_func=image_colors), )
    plt.axis("off")
    plt.show()