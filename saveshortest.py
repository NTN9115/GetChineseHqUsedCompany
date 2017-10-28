#get shortestname
tes=['中国工商银行', '上海国际集团有限公司', '上海国际集团']
def s_s(test = [1,1]):
    c =test[:]
    a = 0
    while a<=len(test)-1 :
        b = 0
        while b<=len(test)-1:
            if a != b and test[a] in test[b] and test[b] not in test[a]:
                try:
                    del c[b]
                except IndexError as e:
                    print(e)
            b = b+1
        a = a+1
    return c
