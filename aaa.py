# coding:utf-8
from bs4 import BeautifulSoup
import urllib2
from province import province

provinceName = raw_input('你想看哪个省市\n')
cityCode = province.get(provinceName)

print cityCode

url1 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/%s.html" % cityCode
print url1


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
print getPage(url1)
