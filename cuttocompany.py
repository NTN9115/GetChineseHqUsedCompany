#cut useless
import re
d = ["吉晓辉", "男", "1955年出生", "工商管理硕士", "高级经济师", "曾任中国工商银行上海浦东分行行长", "党委副书记", "中国工商银行上海市分行副行长", "党委副书记", "中国工商银行上海市分行行长", "党委书记", "上海市政府副秘书长", "上海市金融工作党委副书记", "上海市金融服务办公室主任", "现任上海浦东发展银行股份有限公司董事长", "党委书记", "上海国际集团有限公司董事长", "党委书记", "第十届", "第十一届全国政协委员", "中共上海市第十届委员会委员", "此简介更新于2016-04-30"]
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