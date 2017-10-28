#cut useless
import re
d = ['现任山东中鲁海延远洋渔业有限公司', '月起任山东省中鲁远洋渔业股份有限公司', '曾任山东省水产集团', '曾任山东省水产集团总公司', '山东省水产企业集团', '山东省水产企业集团总公司太平洋渔业公司', '山东省中鲁远洋渔业股份有限公司青岛海延分公司', '青岛海维分公司', '山东省中鲁海延远洋渔业公司', '山东省中鲁远洋渔业股份有限公司']
def cut(a=[]):
    y= []
    x = [0,0,0,0,0]
    for n in a:
        if len(n) >= 4:
            pattern1 = re.compile(u'[\u4e00-\u9fa5]+公司')
            pattern2 = re.compile(u'[\u4e00-\u9fa5]+厂')
            pattern3 = re.compile(u'[\u4e00-\u9fa5]+集团')
            pattern4 = re.compile(u'[\u4e00-\u9fa5]+银行')
            pattern5 = re.compile(u'[\u4e00-\u9fa5]+会社')
            x[0] = pattern1.findall(n)
            x[1] = pattern2.findall(n)
            x[2] = pattern3.findall(n)
            x[3] = pattern4.findall(n)
            x[4] = pattern5.findall(n)
            for xn in x:
                for q in xn:
                    if q not in y:
                        y.append(q)

    return y