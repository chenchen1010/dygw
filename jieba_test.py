
str = "走廊就是卖场北"
print(int(len(str)/2))
print(str[0:2])
print(str[2:85])


# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
#
# import jieba.posseg as pseg
#
# str = '''上午七点三十五分，石神像平常一样离开公寓。虽已进入三月，风还是相当冷，他把下巴埋在围巾里迈步走出。走上马路前，他先瞥了一眼脚踏车停车场。那里放着几辆车，但是没有他在意的绿色脚踏车。'''
#
# words = pseg.cut(str)
# for word, flag in words:
#     print('%s %s' % (word, flag))
