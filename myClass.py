# coding:utf-8
import re

import unittest
import ddt
from time import sleep
from selenium import webdriver


@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    @ddt.data(["something", "noting"], ["one", "noting"])
    @ddt.unpack
    def test_Something(self, first, second):
        dr = self.driver
        dr.get("https://www.baidu.com/s?ie=UTF-8&wd=%s" % first)
        sleep(5)
        assert second not in dr.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()























# “.”在正则表达式中表示除换行符以外的任意字符。
# “\S”它表示的是不是空白符的任意字符。注意是大写字符S。
# 任意字符是用“.”表示，而“*”则不是表示字符，而是表示数量：它表示前面的字符可以重复任意多次（包括0次），只要满足这样的条件，都会被表达式匹配上。
# 这是因为“*”在匹配时，会匹配尽可能长的结果。如果你想让他匹配到最短的就停止，需要用“.*?”。如“I.*?e”，就会得到第二种结果。这种匹配方式被称为懒惰匹配，而原本尽可能长的方式被称为贪婪匹配。
# CommonDiseases = "Hi, I am Shirley Hilton. I am his wife."
# m = re.findall(r"I.*e", CommonDiseases)
# if m:
#     print m
# else:
#     print 'not match'
#
# text1 = "site sea sue sweet see case sse ssee loses"
# m1 = re.findall(r"\bs\S*e\b", text1)
# if m1:
#     print m1
# else:
#     print 'not match'
# import time
#
# print '输入您的电话号码\n'
# input_ = False
# while not input_:
#     try:
#         startTime = time.time()
#         number = str(input())
#         m2 = re.findall(r'\b1[3578][0-9]{9}\b|\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}', number)
#         if m2:
#             input_ = True
#         else:
#             print '请输入正确的手机号码'
#         endTime = time.time()
#         print '耗时：%f'%(startTime-endTime)
#     except:
#         print '请输入正确的手机号码'


# print ';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])

#
# lst_1 = [1,2,3,4,5,6]
# lst_2 = [1,3,5,7,9,11]
# lst_3 = map(None, lst_1)
# print lst_3
# lst_4 = map(None, lst_1, lst_2)
# print lst_4

# import math
#
#
# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def drive(self, distance):
#         print 'need %.2f hour(s)' % (distance / self.speed)
#
#
# class Bike(Vehicle):
#     pass
#
#
# class Car(Vehicle):
#     def __init__(self, speed, fuel):
#         Vehicle.__init__(self, speed)
#         self.fuel = fuel
#
#     def drive(self, distance):
#         Vehicle.drive(self, distance)
#         print 'need %.2f fuels' % (distance * self.fuel)
#
#
# Bike(15.0).drive(100.0)
#
# Car(80.0, 0.012).drive(100.0)
#
# # 求值 (-b±√(b²-4ac))/2a
# a = int()
# b = int()
# c = int()
# i = math.pow(b, 2) - 4 * a * b
# if i <= 0:
#     s = 0
# else:
#     s = math.sqrt(i)
#
# print (-b - s) / 2 * a
# print (s - b) / 2 * a
