import requests
import chardet

url='http://www.sina.com.cn/'
r=requests.get(url)
after_gzip=r.content
print('解压后字符串的编码为:',chardet.detect(after_gzip))
print(after_gzip.decode('UTF-8'))