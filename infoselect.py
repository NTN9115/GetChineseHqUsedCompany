#select useful
import json
with open('Data/hqinfocp01.json') as f:
    allinfo = json.load(f)
cinfo = []
a = 0
t = 0
q = []
while a <= len(allinfo)-1:
    cnum = int(allinfo[a][0])
    x=[]
    b = cnum+1
    while b<=len(allinfo[a])-1:
        try:
            s = allinfo[a][b]
        except IndexError:
            c = 0
        else:
            c = 0
            while c <=len(s)-1:
                if len(s[c])>3:
                    if cnum == 2:
                        t = int(allinfo[a][1] in s[c])+int(allinfo[a][2] in s[c])
                    elif cnum == 3:
                        t = int(allinfo[a][1] in s[c]) + int(allinfo[a][2] in s[c])+int(allinfo[a][3] in s[c])
                    elif cnum ==4:
                        t = int(allinfo[a][1] in s[c]) + int(allinfo[a][2] in s[c]) + int(allinfo[a][3] in s[c])+int(allinfo[a][4] in s[c])
                    q = cnum-t
                    if q!=0:
                        x.append(s[c])
                c = c+1
        b =b +1
    a = a+1
    cinfo.append(x)
with open('Data/hqinfoselect.json','w') as f:
    json.dump(cinfo,f,ensure_ascii=False)