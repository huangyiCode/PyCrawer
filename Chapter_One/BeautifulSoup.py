# Used beautifulSoup to parse html data

from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.baidu.com')
resultData = r.content

# print resultData

soup = BeautifulSoup(resultData, 'lxml', from_encoding='utf-8')

# print soup.p
# It always used like the document.
# print soup
# print soup.span
# print soup.span.input.attrs
# print soup.span.input['name']
# print soup.span['class']
#
# print soup.head.contents
#
# print soup.find_all('a')

from lxml import etree

html = etree.HTML(resultData)
result = etree.tostring(html)
print result

re=html.xpath("//a/@href")
print re
