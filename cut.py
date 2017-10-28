#cut stock name (step2)

import json
import re
comy=['集团','股份']
prov=['中国','北京','天津','上海','重庆','河北','山西','辽宁','吉林','龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南','四川','贵州','云南','陕西','甘肃','青海','台湾','内蒙','广西','西藏','宁夏','新疆','香港','澳门']
hqinfos = []
with open('Data/hqinfo1.json') as f:
    hqinfo = json.load(f)
for hqinf in hqinfo:
    hqin = []
    if hqinf[0][0]+hqinf[0][1] in prov:
        hqin.append(str(len(hqinf[0]) - 1))
        hqin.append(hqinf[0][0] + hqinf[0][1])
        a = 2
        while a <= len(hqinf[0]) - 1:
            hqin.append(hqinf[0][a])
            a = a + 1
    elif comy[0] in hqinf[0][-1:-3]  or comy[1] in hqinf[0][-1:-3]:
        hqin.append(str(2))
        hqin.append(hqinf[0][0] + hqinf[0][1])
        a = 2
        while a <= len(hqinf[0]) - 1:
            hqin.append(hqinf[0][a])
            a = a + 1

    else:
        hqin.append(str(len(hqinf[0])))
        a = 0
        while a <= len(hqinf[0]) - 1:
            hqin.append(hqinf[0][a])
            a = a + 1
    for h in hqinf[1]:
        hq = re.split(r'(?:。|、|,|;|.\s)\s*',h)
        hqin.append(hq)
    hqinfos.append(hqin)

with open('Data/hqinfosplit2.json','w') as f:
    json.dump(hqinfos,f,ensure_ascii=False)