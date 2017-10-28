test= ['中国工商银行', '上海浦东发展银行', '上海国际集团']
test2 = []
def remvnow(te = [],tr =[]):
    a = te[:]
    b = tr[:]
    q = []
    if len(tr)==0:
        return te
    else:
        for ar in a:
            for arr in b:
                if ar not in arr or arr not in ar and arr != '':

                    q.append(ar)
        return q