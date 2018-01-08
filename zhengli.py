# name = []#结果输出list
# for i in range(0,n+1):
# for x in a:
#     # x = x.split()
#     # print(x)
#     if x:#x非空
#         # print("feikong")
#         # print(client.lexer(str(x)))
#         for y in client.lexer(str(x))['items']:##注意！！！这个里面的输入不能是[]空，for循环处理每句话，
#             if y['ne']=='PER':                  #太好时间了，并且后面有地方报错，不便于调试。
#                 name.append(y['item'])
#     # else:
#     #     print("kong")
#
#
# print(name)


# textum =[]
# for d,x in word_dict.items():
#     linshituple = (d,x)
#     textum.append(linshituple)
# print(textum)


#
# text = "东野圭吾是一位很有名的作家"
#
# """ 调用词法分析 """
# list = client.lexer(text)['items']
# print(list)
# for i in range(len(list)):
#     print(list[i]['item'] + " " + list[i]['ne'])#"".join(list[i]['basic_words']

# name = []
# for y in client.lexer(text)['items']:
#     if y['ne']=='PER':
#         name.append(y['item'])
# print(name)