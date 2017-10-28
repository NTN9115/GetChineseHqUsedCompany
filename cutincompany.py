#save list include company and stock name(step3)

import json
from cuttocompany import cut
with open('Data/hqinfosplit2.json') as f:
    allinfo = json.load(f)
a = 0
cpinfo = []

for all in allinfo:
   cnum = int(all[0])
   try:
       sel =  all[cnum+1]
   except IndexError:
       a = a + 1
   else:
       cpin = []
       for b in range(0,cnum+1):
           cpin.append(all[b])
       cpin.append(cut(sel))
       cpinfo.append(cpin)
with open('Data/hqinfocp0.json','w') as f:
    json.dump(cpinfo,f,ensure_ascii=False)





