import requests
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

def fillUnivList(uList,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if (isinstance(tr,bs4.element.Tag)):
            tds = tr.find_all("td")
            uList.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
    return uList

def printUnivList(uList, num):
    tmplt = "{0:^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:^10}"
    print(tmplt.format("排名","学校名称","省市","被引用论文",chr(12288)))
    for i in range(num):
        u = uList[i]
        print(tmplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def getInfoList(infoList, html):
    soup = BeautifulSoup(html, "html.parser")
    dl = soup.find_all("dl")[-1]
    for dd in dl.find_all("dd"):
        print(dd.text)

def main():
#    url = "http://zuihaodaxue.cn/dingjianchengguopaiming2017.html"
    url = "http://www.wuxiph.com/Info/GongGaoLan/Index.html"
    html = getHtmlText(url)
    uInfo = []
    getInfoList(uInfo,html)

 #   html = getHtmlText(url)
  #  fillUnivList(uInfo,html)
   # printUnivList(uInfo,20)

main()