#get a company's hq infomation
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from timerecorder import  TimeCount
def readhq(stock = '000001'):
    ss = TimeCount()
    hq = []
    ss.start()
    try:
        url1 = 'http://stockpage.10jqka.com.cn/' + stock + '/company/'
        html = urlopen(url1)
    except HTTPError:
        print(HTTPError)
    else:
        #bsObj = BeautifulSoup(html.read(),'html.parser',from_encoding='gbk')
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        list = bsObj.find_all('td', {'class': 'mainintro'})
        for namelist in list:
            if namelist.get_text() not in hq:
                hq.append(namelist.get_text().strip('\n'))
    a=ss.stop()
    print(a)
    if a > 10:
        readhq(stock)
    return hq
