import json
from savecp import whatused
from removenow import remvnow
with open('Data/hqinfocp0.json') as f:
    allinfo = json.load(f)
alln = []
for info in allinfo:
    allnn = []
    cnum = int(info[0])
    for a in info[:cnum+1]:
        allnn.append(a)
    b = info[cnum+1]
    n = whatused(b)
    m=remvnow(n[0], n[1])
    print(m)
    allnn.append(n)
    alln.append(allnn)

with open('Data/hqinfocp01.json','w') as f:
    json.dump(alln,f,ensure_ascii=False)