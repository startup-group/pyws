import requests
import re
import bs4
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Failed"

def getJingDianZuoJiaList(myList,html):
    soup = BeautifulSoup(html,"html.parser")
    tbs = soup.find_all("table")
    td = tbs[9].find("td")
    #经典作家
    jingdianzuojia = td.find_parent().find_next_sibling()
    aa = jingdianzuojia.find_all("a")
    for a in aa:
        myList.append(["http://www.kanunu8.com"+a['href'],a.text])
#        print("http://www.kanunu8.com"+a['href'] + "," + a.text)
    return myList

def printList(uList, num):
    tmplt = "{0:^50}\t{1:^10}"
    print(tmplt.format("链接","作家名称"))
    for i in range(num):
        u = uList[i]
#        print(u[0],u[1])
        print(tmplt.format(u[0], u[1], chr(12288)))

def getInfoList(infoList, html):
    soup = BeautifulSoup(html, "html.parser")
    dl = soup.find_all("dl")[-1]
    for dd in dl.find_all("dd"):
        print(dd.text)

def main():
#    url = "http://www.kanunu8.com/"
#    zuojiaList = []
#    html = getHtmlText(url)
#    getJingDianZuoJiaList(zuojiaList,html)
#    printList(zuojiaList,10)
#    getInfoList(uInfo,html)
    url1 = "http://www.wuxiph.com/Info/GongGaoLan/Index.html"
    url3 = "http://www.wuxihospital.com/NEWnew/YuanNaGongGao/Index.html"
    url4 = "http://www.wxfuyou.com/new/Index.html"
    url5 = "http://www.wxtcm.com/News/GongQiGongGao/Index.html"
    try:
        r = requests.get(url1)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find(attrs={'class':'right_bottom'})
        dds = div.findChildren('dd')
        for dd in dds:
            print(dd.findChild('a').text + ' - ' + dd.findChild('span').text)
    except:
        return "Failed"
#        for td in tds:
#            print(td.findChild('a').text + ' - ' + dd.findChild('span').text)

def secondhospital():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    url2 = "http://www.wx2h.com/news/ggindex/index.html"
    r = requests.get(url2, headers = headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.title.string)
    ul = soup.select(".main-fr-box")
    for u in ul:
        aa = u.find_all("a")
        for a in aa:
            print(a.text, a.get("href"))
secondhospital()