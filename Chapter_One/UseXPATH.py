# How to use xpath

re = open('./google.html')
res = re.read()
print res

from bs4 import BeautifulSoup

from lxml import etree

result = etree.HTML(res)

# find all div
resp = result.xpath('//div')

print resp
# find all span after div
resp1 = result.xpath('//div/span')
print resp1

# find all div/span which contain id attribute
resp2 = result.xpath('//div/span[@id]')
print '//div/span[@id]-----%d' % (len(resp2))
print resp2

# find all div/span which contain id attribute is voice-text-f
resp3 = result.xpath('//div/span[@id=\'voice-text-f\']')
print '//div/span[@id=\'voice-text-f\']-----%d' % (len(resp3))

# find all div/span which contain id attribute is voice-text-f and used class content
resp4=result.xpath('//div/span[@id=\'voice-text-f\']/@class')
print resp4

# find all div/span which contain id attribute is voice-text-f and used them parent
resp5=result.xpath('////div/span[@id=\'voice-text-f\']/parent::*')
print resp5

# ...