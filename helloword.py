# coding:utf-8
import codecs
import sys
import urllib2
import json
from city import city

reload(sys)
sys.setdefaultencoding('utf-8')

cityName = raw_input('您想查看那个城市的天气？\n')
cityCode = city.get(cityName)
if cityCode:
    try:
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % cityCode
        content = urllib2.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = '%s\n%s ~ %s' % (result['weather'], result['temp1'], result['temp2'])
        print str_temp
    except:
        print '查询失败'
else:
    print '没有找到该城市'






# from random import randint
#
# name = raw_input('请输入你的名字：')
#
# f = file('scores.txt')
# #score = f.read().split()
# lines = f.readlines()
# f.close()
#
# scores = {}
# for l in lines:
#     s = l.split()
#     scores[s[0]] = s[1:]
# score = scores.get(name)
# # print score
# if score is None:
#     score = [0, 0, 0]
#
# # 游戏轮数
# game_times = int(score[0])
# # 每轮用total_times次猜出答案
# min_times = int(score[1])
# # 每轮用total_times次猜出答案
# total_times = int(score[2])
# if game_times > 0:
#     avg_times = float(total_times) / game_times
# else:
#     avg_times = 0
# print '%s 你已经玩儿了%d轮，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times)
#
# num = randint(1, 100)
# print '请输入您的答案'
# times = 0
# bingo = False
# while not bingo:
#     times += 1
#     try:
#         answer = input('answer：')
#     except:
#         print '游戏结束'
#         bingo = True
#     if answer < num:
#         print 'too small'
#     if answer > num:
#         print 'too big'
#     if answer == num:
#         print 'bingo'
#         bingo = True
# if game_times == 0 or times < min_times:
#     min_times == times
# total_times += times
# game_times += 1
# scores[name] = [str(game_times), str(min_times), str(total_times)]
#
# result = ''
# for n in scores:
#     line = n + ' ' + ' '.join(scores[n]) + '\n'
#     result += line
#
# # print result
# f = file('scores.txt', "w")
# f.write(result)
# f.close()
#







# from random import choice
# score = [0, 0]
# direction = ['左', '中', '右']
# def kick():
#     print '==== 进攻! ===='
#     print '选择进攻方向:左, 中, 右'
#     you = raw_input()
#     print '进攻' + you
#     com = choice(direction)
#     print '电脑防守' + com
#     if you != com:
#         print '进球!'
#         score[0] += 1
#     else:
#         print '防守成功...'
#     print '得分: %d(you) - %d(com)\n' % (score[0], score[1])
#     print '==== 防守! ===='
#     print '选择防守方向:左, 中, 右'
#     you = raw_input()
#     print '防守' + you
#     com = choice(direction)
#     print '电脑进攻' + com
#     if you == com:
#         print '防守成功!'
#     else:
#         print '进球...'
#         score[1] += 1
#     print '得分: %d(you) - %d(com)\n' % (score[0], score[1])
# for i in range(5):
#     print '==== Round %d ====' % (i + 1)
#     kick()
#     while score[0] == [1]:
#         i += 1
#         print '==== Round %d ====' % (i + 1)
#         kick()
# if score[1] < score[0]:
#     print '你赢了!'
# else:
#     print '你输了.'
