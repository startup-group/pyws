import requests
from bs4 import BeautifulSoup

url = 'http://www.itest.info/courses'
soup = BeautifulSoup(requests.get(url).text,'html.parser')
for course in soup.find_all('h4'):
    print(course.text)

url = 'https://www.v2ex.com/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

for span in soup.find_all('span', class_='item_hot_topic_title'):
    print(span.find('a').text, span.find('a')['href'])