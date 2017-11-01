import json
import csv
with open('Data/final.json') as f:
    allcoms = json.load(f)
companies =[]
headers = ['companies']
for com in allcoms:
    cp = (com,)
    companies.append(cp)
with open('Data/stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(companies)