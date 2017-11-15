# coding:utf-8
"""
                              _.._        ,------------.
                           ,'      `.    ( We want you! )
                          /  __) __` \    `-,----------'
                         (  (`-`(-')  ) _.-'
                         /)  \  = /  (
                        /'    |--' .  \
                       (  ,---|  `-.)__`
                        )(  `-.,--'   _`-.
                       '/,'          (  Uu",
                        (_       ,    `/,-' )
                        `.__,  : `-'/  /`--'
                          |     `--'  |
                          `   `-._   /
                           \        (
                           /\ .      \.  cat
                          / |` \     ,-\
                         /  \| .)   /   \
                        ( ,'|\    ,'     :
                        | \,`.`--"/      }
                        `,'    \  |,'    /
                       / "-._   `-/      |
                       "-.   "-.,'|     ;
                      /        _/["---'""]
                     :        /  |"-     '
                     '           |      /
                                 `     |
"""
import re
import time
from imp import reload

from bs4 import BeautifulSoup
import urllib2
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def openUrl(x):
    url = 'http://tuodanyy.com/m/xmsick.html?sicknessid=%d' % x
    f = urllib2.urlopen(url)
    s = f.read().lower().decode('utf8')
    soup = BeautifulSoup(s, "html.parser")
    return soup


def getTitle(soup):
    t = ''
    for item in str(soup.title):
        if item in r'''0-9{}%a-z'<>()?$+:&;|#!/"=-_.''':
            continue
        t += item
    return t


def getTxt(soup, div, class_):
    dt = ''
    for k in soup.find_all(div, class_=class_):
        k = str(k)
        dt += k
    return dt


def getTup(soup, div, class_):
    list = soup.find_all(div, class_=class_)
    for tp in list:
        jokes = tp.find('img')
        link = jokes.get('src')
        return link


'''网址ID起始'''
begin = int(1001)
over = int(1002)
for i in range(begin, over):  # 1330
    # print time.strftime('\n%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ':正在执行ID为----->%d 的页面' % i
    p = openUrl(i)
    title = getTitle(p)
    text = str(getTxt(p, 'div', 'n_p2'))
    if None != title and None != text:
        filePN = 'CommonDiseases/' + '%d' % i + title + '.txt'
        with codecs.open(filePN, 'wb', 'utf8') as f:  # 文件写入
            f.write(title + "\n" + text)
        time.sleep(1.5)
        if i == over - 1:
            pass
            # print '------------------------------------>'
            # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ':执行完毕，共执行 %d 条' % (over - begin)
            # print '<------------------------------------'
    else:
        time.sleep(1.5)
        print('------------------------------------------------------------------------>>>>>>>>>>>>')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ':第 %d 条执行失败' % i)
        print('<<<<<<<<<<<<------------------------------------------------------------------------')
