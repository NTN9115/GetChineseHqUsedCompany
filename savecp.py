#find used company in list
import re
from removenow import remvnow
from saveshortest import s_s
test = ["曾任中国工商银行", "中国工商银行", "现任上海浦东发展银行股份有限公司","上海浦东发展银行", "现任上海浦东发展银行", "上海国际集团有限公司", "上海国际集团"]
def whatused(test=[]):
    str_pattern = ['','','','','','']
    str_pattern[0] = '现任|今在|今任'
    str_pattern[1] = '北京省|天津省|上海省|重庆省|河北省|山西省|辽宁省|吉林省|龙江省|江苏省|浙江省|安徽省|福建省|江西省|山东省|河南省|湖北省|湖南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|内蒙省|广西省|西藏省|宁夏省|新疆省|香港省|澳门中国|北京|天津|上海|重庆|河北|山西|辽宁|吉林|龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾|内蒙|广西|西藏|宁夏|新疆|香港|澳门'
    str_pattern[2] = '中国'
    str_pattern[3] = '历任|曾任|为|在|月任|曾就职于|出任|先生任'
    str_pattern[4] = '原名|一直担任|'
    str_pattern[5] = '有限公司'
    pattern1 = re.compile(str_pattern[0])
    pattern2 = re.compile(str_pattern[1])
    pattern3 = re.compile(str_pattern[2])
    pattern4 = re.compile(str_pattern[3])
    pattern5 = re.compile(str_pattern[4])
    all1 = []
    notused = []
    used = []
    for t in test:
        m1 = pattern1.search(t)
        m2 = pattern2.search(t)
        m3 = pattern3.search(t)
        m4 = pattern4.search(t)
        m5 = pattern5.search(t)
        m6 = (str_pattern[5] == t)
        if m1:
            s = t[m1.end():]
            if s not in notused:
                notused.append(s)
        elif m2:
            s = t[m2.start():]
            if s not in used:
                used.append(s)
        elif m3:
            s = t[m3.start():]
            if s not in used:
                used.append(s)
        elif m4:
            s = t[m4.end():]
            if s not in used:
                used.append(s)
        elif m5 or m6:
            n1 = 1
        elif t not in used:
            used.append(t)
    all1.append(s_s(used))
    all1.append(s_s(notused))
    return all1