
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']

import matplotlib.pyplot as plt

from wordcloud import WordCloud
import os

file_name_list=[]
file_names = os.listdir('./output')
for x in file_names:
    if 'name' in x:
        file_name_list.append(x)

file_name_list = [x.strip('.txt') for x in file_name_list]
file_name_list = [x.strip('name_') for x in file_name_list]
print(file_name_list)

for x in file_name_list:

    word_lst = []
    word_dict= {}
    with open('./output/name_'+x+'.txt') as wf,open("./figout/cp_"+x+".txt",'w') as wf2: #//打开文件

        for word in wf:
            word_lst.append(word.split(' ')) #//使用逗号进行切分
            for item in word_lst:
                 for item2 in item:
                    if item2 not in word_dict: #//统计数量
                        word_dict[item2] = 1
                    else:
                        word_dict[item2] += 1

        # for key in word_dict:
        #     print(key,word_dict[key])
        #     wf2.write(key+' '+str(word_dict[key])+'\n')# //写入文档
        #

        dict = sorted(word_dict.items(), key=lambda d:d[1], reverse = True)
        for key2 in dict:
            wf2.write(key2[0]+' '+str(key2[1])+'\n')# //写入文档
    # print(dict)

    # print(word_dict)

    wordcloud = WordCloud(background_color="white",width=1000, height=860, font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",margin=2).generate_from_frequencies(word_dict)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title("《"+x+"》人物词云图")
    # plt.show()
    wordcloud.to_file("fig_"+x+".jpg")
