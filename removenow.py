test= ['中国工商银行', '上海浦东发展银行', '上海国际集团']
test2 = []
def remvnow(te = [],tr =[]):
    a = te[:]
    b = tr[:]
    q = []
    try:
        b1 = b[0]
    except IndexError :
        return te
    if len(tr)==0:
        return te
    else:
        for ar in a:
            if b1 not in ar:
                q.append(ar)
    return q
