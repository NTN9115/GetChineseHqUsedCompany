#get shortestname
tes=['中国工商银行', '上海国际集团', '上海浦东发展银行', '上海国际集团有限公司']
def s_s(test = []):
    c = []
    d = []
    tnn = sorted(test,key=len)
    try:
        c.append(tnn[0])
    except IndexError as e:
        print(e)
    for tn in tnn[1:]:
        n = 0
        for cc in c:
            if cc not in tn:
                n = n+1

        if n == len(c) and tn not in c:
            c.append(tn)
    for nn in c:
        if len(nn) > 3:
            d.append(nn)
    return d
print(s_s(tes))