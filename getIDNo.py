# coding:utf-8
from imp import reload
import urllib2
import sys
import re

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
# 省
province = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北",
            "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆"]
# 市
city = ["市辖区", "县"]
# 区
area = ["东城区", "西城区", "崇文区", "宣武区", "朝阳区", "丰台区", "石景山区", "海淀区", "门头沟区", "房山区", "通州区", "顺义区"]
# 年
year = ["1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993"]
# 月
month = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
# 日
day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
       "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
# 性别
sex = ["男", "女"]
while True:
    provinceNo = input("请输入0-%d选择省份:" % (len(province)-1))
    if provinceNo <= len(province)-1:
        break
while True:
    cityNo = input("请输入0-%d选择市区(0市辖区，1县):" % (len(city) - 1))
    if cityNo <= len(city)-1:
        break
while True:
    areaNo = input("请输入0-%d选择区县:" % (len(area) - 1))
    if areaNo <= len(area)-1:
        break
while True:
    yearNo = input("请输入0-%d选择年份:" % (len(year) - 1))
    if yearNo <= len(year)-1:
        break
while True:
    monthNo = input("请输入0-%d选择月份:" % (len(month) - 1))
    if monthNo <= len(month)-1:
        break
if monthNo == 1:
    day2 = len(day) - 4
elif monthNo == 0 or monthNo == 2 or monthNo == 4 or monthNo == 6 or monthNo == 7 or monthNo == 9 or monthNo == 11:
    day2 = len(day)-1
else:
    day2 = len(day) - 2
while True:
    dayNo = input("请输入0-%d选择天数:" % day2)
    if dayNo <= day2:
        break
while True:
    sexNo = input("请输入(0男、1女)选择性别:")
    if sexNo == 1 or sexNo == 0:
        break
try:
    val = 'province=' + province[provinceNo] + '&city=' + city[cityNo] + '&area=' + area[areaNo] + '&year=' + year[yearNo] + '&month=' + month[monthNo] + '&day=' + day[dayNo] + '&sex=' + sex[sexNo]
except ():
    print("输入错误")
url1 = 'http://www.welefen.com/lab/identify?%s' % val
print('第三方网址：' + url1)


# 读取网页内容
def getPage(url, code='UTF-8', driver_='Chrome'):
    # httpHandler = urllib2.HTTPHandler(debuglevel=1)
    # httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    # opener = urllib2.build_opener(httpHandler, httpsHandler)
    # urllib2.install_opener(opener)
    request = urllib2.Request(url)
    request.add_header("User-Agent", driver_)
    response = urllib2.urlopen(request)
    s = response.read().lower().decode(code)
    soup = BeautifulSoup(s, "html.parser")
    return soup


# 获取网页tr下class为provincetr的所有内容
def getContent(soup_):
    dt = ''
    for k in soup_.find_all('p'):
        k = str(k)
        dt += k
    return dt


# 过滤不需要的字符
def convertContent(txt):
    t = ''
    for item in str(txt):
        if item in r'''{}%qwertyuiopasdfghjklzcvbnmz'<>()?$+:&;|#!/"=-_''':
            continue
        t += item
    return t


try:
    match = input('请输入取值次数，每次取5条\n')
    degree = 5*int(match)
    areas = '以下是' + str(degree) + '个地址：' + province[provinceNo] + ' ' + city[cityNo] + ' ' + area[areaNo]
    date = ' 出生日期：' + year[yearNo] + '年' + month[monthNo] + '月' + day[dayNo] + '日 性别' + sex[sexNo] + '的身份证号码'
    print(areas + date)
    for i in range(0, int(match)):
        soup = getPage(url1)
        print(re.sub(r' 22x', ' IDNo:', convertContent(getContent(soup))))
except():
    print('发生了错误')
