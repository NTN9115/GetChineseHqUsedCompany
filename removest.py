#remove english character
import json
with open('stocks1.json') as f:
    stocks1 = json.load(f)
stocks=[]

for stock1 in stocks1:
    stock = []
    for stock0 in stock1:
        stock.append(stock0.strip('*STAB'))
    stocks.append(stock)
with open('stock2.json','w') as f:
    json.dump(stocks,f,ensure_ascii=False)