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
    url = "http://www.kanunu8.com/"
    zuojiaList = []
    html = getHtmlText(url)
    getJingDianZuoJiaList(zuojiaList,html)
    printList(zuojiaList,10)
#    getInfoList(uInfo,html)

main()