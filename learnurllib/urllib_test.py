from urllib import request
response = request.urlopen("http://www.cnblogs.com/Lands-ljk/p/5447127.html")
page = response.read()
page = page.decode('utf-8')
print(page)