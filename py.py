#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from random import choice
# # noinspection PyBroadException
# try:
#     while True:
#         answer = raw_input('输入 石头、剪子、布,输入"end"结束游戏:')
#         wa = ['石头', "剪子", "布"]
#         wina = choice(wa)
#         if (answer not in wa) and (answer == 'end'or answer == 'END'):
#             print ("\n游戏退出中...")
#             break
#         elif answer not in wa:
#             print ("输入错误，请重新输入！")
#         elif answer == wina:
#             print ("电脑出了： " + wina + "，平局！")
#         elif (answer == '石头' and wina == '剪子') or (answer == '剪子' and wina == '布') or (answer == '布' and wina == '石头'):
#             print ("电脑出了： " + wina + "，你赢了！")
#         elif (answer == '石头' and wina == '布') or (answer == '剪子' and wina == '石头') or (answer == '布' and wina == '剪子'):
#             print ("电脑出了： " + wina + "，你输了！")
# except:
#     print ("\n游戏结束！")
#
import urllib
url = 'http://www.freebuf.com/articles'
globalcontent = urllib.urlopen(url).read()
news_start = globalcontent
print(news_start)
count = 1
while count <= 2:
    # noinspection PyBroadException
    try:
        news_inner_head = news_start.find('<dt>\n<a href=')
        news_inner_tail = news_start.find('.html')
        news_inner_url = news_start[news_inner_head + 13:news_inner_tail + 5]
        print(news_inner_url)
        news_start = news_start[news_inner_tail + 5:]

        filename = news_inner_url[-10:]
        urllib.urlretrieve(news_inner_url, filename)
        count += 1
    except:
        print('Download Failed!')
        break
    finally:
        if count == 2:
            break
