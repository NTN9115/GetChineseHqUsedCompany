#cut stock name (step2)

import json
import re
comy='集团|股份|国际'
ty = '路桥|机场|高速'
prov='中原|中国|北京|天津|上海|重庆|河北|山西|辽宁|吉林|龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾|内蒙|广西|西藏|宁夏|新疆|香港|澳门'
excp='国际实业|国际医学|视觉中国|天海投资'
hqinfos = []
pattern1 = re.compile(comy)
pattern2 = re.compile(prov)
pattern3 = re.compile(ty)
pattern4 = re.compile(excp)
with open('Data/hqinfo1.json') as f:
    hqinfo = json.load(f)
for hqinf in hqinfo:
    hqin = []
    m1 = pattern1.search(hqinf[0])
    m2 = pattern2.search(hqinf[0])
    m3 = pattern3.search(hqinf[0])
    m4 = pattern4.search(hqinf[0])
    if m4:
        hqin.append(str(len(hqinf[0])))
        print(hqinf[0])
        for ne in hqinf[0]:
            hqin.append(ne)
    else:
        if m1:
            hqin.append(str(len(hqinf[0])-2))
            for n11 in hqinf[0][:m1.start()]:
                hqin.append(n11)
        elif m2:
            if not m3:
                hqin.append(str(len(hqinf[0])-2))
                for n22 in (hqinf[0][m2.end():]):
                    hqin.append(n22)
            else:
                hqin.append(str(len(hqinf[0])-2))
                hqin.append(hqinf[0][m2.start():m2.end()])
                hqin.append(hqinf[0][m2.end()])
        else:
            hqin.append(str(len(hqinf[0])))
            for n33 in hqinf[0]:
                hqin.append(n33)
    for h in hqinf[1]:
        hq = re.split(r'(?:。|、|,|;|.\s)\s*', h)
        if h not in hqin:
            hqin.append(hq)
    hqinfos.append(hqin)

with open('Data/hqinfosplit2.json', 'w') as f:
    json.dump(hqinfos, f, ensure_ascii=False)