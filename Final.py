import json
with open('Data/hqinfoselect.json') as f:
    allcps = json.load(f)
cps = []
for allcp in allcps:
    for cp in allcp:
       if cp !='' and cp not in cps:
           cps.append(cp)
with open('Data/final.json','w') as f:
    json.dump(cps,f,ensure_ascii=False)