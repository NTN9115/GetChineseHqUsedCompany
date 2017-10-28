# make a list of company and hq (step1)
import json
from readacompyhq import readhq
with open('Data/stock2.json') as f:
    stocks = json.load(f)
allhqinfo = []
for stock in stocks:
    hq = []
    print(stock[1])
    hq.append(stock[0])
    a = stock[1]
    hq.append(readhq(a))
    if hq not in allhqinfo:
        print(hq)
        allhqinfo.append(hq)
with open('Data/hqinfo1.json','w') as f:
    json.dump(allhqinfo,f,ensure_ascii=False)