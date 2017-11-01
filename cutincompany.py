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

       cpin.append(all1[1:cnum+1])
       for b in all1[cnum+1:]:
           cpin1.append(cut(b))
       for a in cpin1:
           for nx in a:
               cpin2.append(nx)
   cpin.append(cpin2)
   cpinfo.append(cpin)

with open('Data/hqinfocp0.json','w') as f:
    json.dump(cpinfo,f,ensure_ascii=False)





