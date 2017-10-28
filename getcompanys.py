import json
from savecp import whatused
from removenow import remvnow
with open('Data/hqinfocp0.json') as f:
    allinfo = json.load(f)
alln = []
for info in allinfo:
    allnn = []
    cnum = int(info[0])
    for inf in info[0:cnum+1]:
        print(inf)
        allnn.append(inf)
    try:
        aq = info[cnum+1]
    except IndexError as e:
        print(e)
    else:
        print(aq)
        a = remvnow(whatused(aq)[0],whatused(aq)[1])
        print(a)
        allnn.append(a)
    alln.append(allnn)
with open('Data/hqinfocp01.json','w') as f:
    json.dump(alln,f,ensure_ascii=False)