#cut useless

import re

d = ["高国富", "男", "1956年出生厂厂", "研究生学历", "博士学位", "高级经济师职称", "曾任上海外高桥保税区开发(控股)公司公司总经理", "上海外高桥保税区管委会副主任", "上海万国证券公司代总裁", "上海久事公司总经理", "上海市城市建设投资开发总公司总经理", "中国太平洋保险(集团)股份有限公司党委书记", "董事长", "现任上海浦东发展银行股份有限公司党委书记", "第十二届全国政协委员", "伦敦金融城中国事务顾问委员会委员", "中欧国际工商学院理事会成员", "国际顾问委员会委员", "上海交通大学安泰经济管理学院顾问委员会委员", "此简介更新于2017-06-02"]

def cut(a=[]):
    y =[]
    z =[]
    pattern1 = re.compile(u'[\u4e00-\u9fa5]+?公司')
    pattern2 = re.compile(u'[\u4e00-\u9fa5]+?银行')
    pattern3 = re.compile(u'[\u4e00-\u9fa5]+?厂')
    pattern4 = re.compile(u'[\u4e00-\u9fa5]+?会社')
    pattern5 = re.compile(u'[\u4e00-\u9fa5]+?集团')

    for a1 in a:
        a1 = re.sub(r'\(.*\)','',a1)
        if len(a1) >= 4 and a1!='':
            if '集团' in a1:
                x = pattern5.findall(a1)
                if x not in y and x!=[] and len(x[0])>= 4:
                    y.append(x[0])
            elif '银行' in a1:
                x= pattern2.findall(a1)
                if x not in y and x!=[] and len(x[0])>= 4:
                    y.append(x[0])
            elif '厂' in a1:
                x = pattern3.findall(a1)
                if x not in y and x!=[] and len(x[0])>= 4:
                    y.append(x[0])
            elif '公司' in a1 and '子公司' not in a1 and '这些公司' not in a1 and '本公司' not in a1 and '任公司' not in a1 and '在公司' not in a1:
                x=pattern1.findall(a1)
                if x not in y and x!=[] and len(x[0])>= 4 and x[0]!='投资有限公司' and x[0]!='现担任公司' and x[0]!='月起担任公司' and x[0]!='这些公司' and x[0]!='月至今公司':
                    y.append(x[0])

            elif '会社' in a1:
                x = pattern4.findall(a1)
                if x not in y and x!=[] and len(x[0])>= 4:
                    y.append(x[0])
    for y1 in y:
        if ('子公司' or '这些公司' or '本公司' or '任公司' or '在公司') not in y1:
            z.append(y1)
    return z
#print(cut(d))