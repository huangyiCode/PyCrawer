import requests

from lxml import etree
import chardet
import json
import csv

response=requests.get('http://seputu.com')
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'
headers={'User-Agent':user_agent}
content=response.content.decode('utf-8')
print content
html=etree.HTML(content)
names=html.xpath('//ul/li/a/text()')
urls=html.xpath('//ul/li/a/@href')
content=[]
for index in range(len(names)):
    content.append({"name":names[index],"url":urls[index]})


# Save data with JSON file.
with open('daoMu.json','wb') as fileWrite:
     json.dump(content,fp=fileWrite,indent=4)

#Save data with CSV file.
csvHeaders=['NAME','PATH']

rows=[]

for index in range(len(names)):
    NAME=names[index].encode('utf-8')
    PATH=urls[index]
    rows.append((NAME,PATH))


with open('daoMu.csv','w') as fileWrite:
    fCSV = csv.writer(fileWrite,)
    fCSV.writerow(csvHeaders)
    fCSV.writerows(rows)
    fileWrite.close()









