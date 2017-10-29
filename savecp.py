#find used company in list
import re
from removenow import remvnow
from saveshortest import s_s
test = ["曾任中国工商银行", "中国工商银行", "现任上海浦东发展银行股份有限公司","上海浦东发展银行", "现任上海浦东发展银行", "上海国际集团有限公司", "上海国际集团"]
def whatused(test=[]):
    str_pattern = [a for a in range(0,100)]
    str_pattern[0] = '现任|今在|今任|加盟|现担任|并任|兼任'
    str_pattern[1] = '深圳|大连|日本|英国|美国|宁波|北京省|天津省|上海省|重庆省|河北省|山西省|辽宁省|吉林省|龙江省|江苏省|浙江省|安徽省|福建省|江西省|山东省|河南省|湖北省|湖南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|内蒙省|广西省|西藏省|宁夏省|新疆省|香港省|澳门中国|北京|天津|上海|重庆|河北|山西|辽宁|吉林|龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾|内蒙|广西|西藏|宁夏|新疆|香港|澳门'
    str_pattern[2] = '中国'
    str_pattern[3] = '历任|曾任|为|在|月任|职于|出任|先生任|年任|月起任|后任|日担任|年在|曾参与'
    str_pattern[4] = '原名|一直担任|大学|分公司|货币银行|从事公司|直属子公司|副厂|子公司|负责公司|本行|香港上市公司|中国有限公司|电脑公司|中国银行|个人银行|多家上市公司|加入公司'
    str_pattern[5] = '有限公司'
    str_pattern[6] = '有限责任公司'
    str_pattern[7] = '营销公司'
    str_pattern[8] = '上市公司'
    str_pattern[9] = '股份有限公司'
    str_pattern[10] = '投资集团'
    str_pattern[11] = '基金公司'
    str_pattern[12] = '中国公司'
    str_pattern[13] = '产品公司'
    str_pattern[14] = '个人银行'
    str_pattern[15] = '担任公司'
    str_pattern[16] = '拟上市公司'
    str_pattern[17] = '株式会社'



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
        m7 = (str_pattern[6] == t)
        m8 = (str_pattern[7] == t)
        m9 = (str_pattern[8] == t)
        m10 = (str_pattern[9] == t)
        m11 = (str_pattern[10] == t)
        m12 = (str_pattern[11] == t)
        m13 = (str_pattern[12] == t)
        m14 = (str_pattern[13] == t)
        m15 = (str_pattern[14] == t)
        m16 = (str_pattern[15] == t)
        m17 = (str_pattern[16] == t)
        m18 = (str_pattern[17] == t)
        if m1:
            s = t[m1.end():]
            if s not in notused:
                notused.append(s)
        elif m4:
            s = t[m4.end():]
            if s not in used:
                used.append(s)
        elif m2:
            s = t[m2.start():]
            if s not in used:
                used.append(s)
        elif m3:
            s = t[m3.start():]
            if s not in used:
                used.append(s)
        elif m5 or m6 or m7 or m8 or m9 or m10 or m11 or m12 or m13 or m14 or m15 or m16 or m17 or m18\
                :
            n1 = 1
        elif t not in used:
            used.append(t)
    all1.append(s_s(used))
    all1.append(s_s(notused))
    return all1
#print(whatused(test))