# urllib urllib2

import urllib2

# get
response = urllib2.urlopen('http://www.zhihu.com')
html = response.read()
# print html

# post

import urllib

url = 'http://www.xxxx.com/login'
postdata = {'username': 'Mike', 'password': 'pwd'}
# data = urllib.urlencode(postdata)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# html = response.read()

# user agent


# set-header


# Cookie handler

# time out

# response code

# redirected

# proxy

# httplib/urllib -------> the steps of http request

# Requests ------->best solution of http request

# chardet -------->to show encoding info

import requests
import chardet

r = requests.get('http://www.baidu.com')
print r.content
print 'text--->' + r.text
print 'encoding--->' + r.encoding
r.encoding = 'utf-8'
print 'text--->' + r.text
print chardet.detect(r.content)
print r.status_code
print r.headers
print r.headers.get('content-type')
print r.url # redirected
print r.history  #response history

