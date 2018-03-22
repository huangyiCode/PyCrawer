# https://www.jd.com/

import requests
import chardet

from lxml import etree


user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'
headers={'User-Agent':user_agent}
response=requests.get('http://www.dytt8.net/html/gndy/dyzz/20180121/56160.html',headers)

resu=response.content
print response.content
print type(response.content)
print chardet.detect(response.content)
print resu

# html=etree.HTML(response.content)
# lis=html.xpath('//a/@href')

# print  lis