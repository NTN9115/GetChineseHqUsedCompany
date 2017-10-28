#get stocks name
import json
import csv
from lxml import etree
import requests
stocks = []
stock = []
with open('Data/ShangshenAB20171027.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        stock = []
        szs = row['stocknum']
        url = 'http://stockpage.10jqka.com.cn/'+szs+'/'
        r = requests.get(url)
        selector = etree.HTML(r.text)
        links = selector.xpath('//*[@id="in_squote"]/div/h1/a[1]/strong')
        for link in links:
            stock.append(link.text)
            stock.append(szs)
        print(szs)
        stocks.append(stock)

with open('Data/stocks1.json','w') as f:
    json.dump(stocks,f,ensure_ascii=False)