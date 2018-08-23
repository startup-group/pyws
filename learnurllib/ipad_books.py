import requests
import re
import os
import pickle
import bs4
from bs4 import BeautifulSoup


def main():
    url1 = "https://bbs.feng.com/thread-htm-fid-224-page-"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    data = open("testfile//testbook.txt", "w")
    count = 1
    while (count < 50):
        count = count + 1
        if (count % 5 == 0):
            print("data.flush")
            data.flush()
        url = url1 + str(count) + ".html"
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, "html.parser")
            items = soup.find_all(id=re.compile("normalthread_"))
            for item in items:
                aa = item.select("th > a")
                try:
                    data.write(aa[0].text + ",https://bbs.feng.com/" + aa[0].get("href") + "\n")
                # print(aa[0].text,",https://bbs.feng.com/"+aa[0].get("href"))
                except:
                    print(aa[0].text, ",https://bbs.feng.com/" + aa[0].get("href"))
        except:
            data.close()
            print("Hello Failed")
            return "Failed"
    data.close()


main()
