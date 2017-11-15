# coding:utf-8

import urllib2
import sys
import re

from bs4 import BeautifulSoup
from province import province

reload(sys)
sys.setdefaultencoding('utf-8')

url1 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html'

# 读取网页内容
def getPage(url, code='gb2312', driver_='Chrome'):
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    request = urllib2.Request(url)
    request.add_header("User-Agent", driver_)
    response = urllib2.urlopen(request)
    s = response.read().lower().decode(code)
    soup = BeautifulSoup(s, "html.parser")
    return soup

# 获取网页tr下class为provincetr的所有内容
def getContent(soup_, div, class_):
    dt = ''
    for k in soup_.find_all(div, class_=class_):
        k = str(k)
        dt += k
    return dt

# 过滤不需要的字符
def convertContent(txt):
    t = ''
    for item in str(txt):
        if item in r'''{}%a-z'<>()?$+:&;|#!/"=-_''':
            continue
        t += item
    return t

# # 正则匹配需要的字符
# content = convertContent(str(getContent(getPage(url1), 'tr', 'provincetr')))
# CommonDiseases = re.sub(r"\n[\s| ]*\n", '\n',re.sub(r'""', '', re.sub(r''' ''', '"\n"', re.sub(r'''\.''', '.html":"', content))))
#
# # 写入文件
# f = file('province.py', 'w')
# f.write('# coding:utf-8\nprovince = {\n'+CommonDiseases + '"\n}')
# f.close()

provinceName = raw_input('你想看哪个省市\n')
path1 = province.get(provinceName)
url2 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/%s.html" % path1
path2 = getPage(url2).a.get('href')
print path2 + 'path2-----------------------------------------'
url3 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/%s" % path2
path3 = getPage(url3).a.get('href')
print path3 + 'path3-----------------------------------------'
url4 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/%s" % (path1+"/"+path3)
path4 = getPage(url4).a.get('href')
print path4 + 'path4-----------------------------------------'
url5 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/%s" % (path1+"/01/"+path4)
path5 = getPage(url5).tr
print path5 + 'path5-----------------------------------------'


# http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/11/01/01/110101001.html
# http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/11/01/110101.html---path3
# http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/11/1101.html---path2
# http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/11.html---path1
# http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html

# try:
#     url1 = 'http://m.weather.com.cn/data5/city.xml'
#     content1 = urllib2.urlopen(url1).read()
#     provinces = content1.split(',')
#     print provinces
#     result = 'city = {\n'
#
#     url = 'http://m.weather.com.cn/data3/city%s.xml'
#     for p in provinces:
#         p_code = p.split('|')[0]
#         url2 = url % p_code
#         print url2
#         content2 = urllib2.urlopen(url2).read()
#         print content2
#         cities = content2.split(',')
#         print cities
#         for c in cities[:3]:
#             c_code = c.split('|')[0]
#             url3 = url % c_code
#             content3 = urllib2.urlopen(url3).read()
#             print content3
#             districts = content3.split(',')
#             print districts
#             for d in districts:
#                 d_pair = d.split('|')
#                 d_code = d_pair[0]
#                 name = d_pair[1]
#                 url4 = url % d_code
#                 content4 = urllib2.urlopen(url4).read()
#                 print content4
#                 try:
#                     CommonDiseases = content4.split('|')[1]
#                     line = "    '%s': '%s',\n" % (name, CommonDiseases)
#                 except:
#                     pass
#                 result += line
#     result += '}'
#     f = file('city.py', 'w')
#     f.write(result)
#     f.close()
# except:
#     print '遇到错误啦，提前结束！'
