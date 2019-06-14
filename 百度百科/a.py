import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0(Windows;U;Windows NT 6.0 x64;en-US;rv:1.9pre)Gecko/2008072421 Minefield/3.0.2pre"}
r=requests.get("https://baike.baidu.com/",headers=headers)
html=r.text
bsObj=BeautifulSoup(html)

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])