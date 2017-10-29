#save list include company and stock name(step3)

import json
from cuttocompany import cut
with open('Data/hqinfosplit2.json') as f:
    allinfo = json.load(f)
a = 0
cpinfo = []

for all1 in allinfo:
   cnum = int(all1[0])
   try:
       sel =  all1[cnum+1]
   except IndexError as e:
       print(all1[:cnum+1])
       print(e)
   else:
       cpin = []
       cpin1 = []
       cpin2 =[]
       for b in range(0,cnum+1):
           cpin.append(all1[b])
       for b in all1[cnum+1:]:
           cpin1.append(cut(b))
       for b in cpin1:
           for nx in b:
               cpin2.append(nx)
   cpin.append(cpin2)
   cpinfo.append(cpin)

with open('Data/hqinfocp0.json','w') as f:
    json.dump(cpinfo,f,ensure_ascii=False)





