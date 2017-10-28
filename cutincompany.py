#save list include company and stock name

import json
from cuttocompany import cut
with open('Data/hqinfosplit1.json') as f:
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
       for b in range(0,cnum+1):
           cpinfo.append(all[b])
       cpinfo.append(cut(sel))

print(cpinfo)




