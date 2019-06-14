import requests
from bs4 import BeautifulSoup

url='http://w3school.com.cn/'
r=requests.get(url)
r.encoding='gbk'
soup=BeautifulSoup(r.text,"lxml")
xx=soup.find('div',id='d1').h2.text
print(xx)