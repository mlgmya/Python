import requests
from lxml import etree
from bs4 import BeautifulSoup
import MySQLdb


def get_page(start_num):
    url="https://movie.douban.com/top250?start=%s&filter=" %start_num
    res=requests.get(url)
    tree=etree.HTML(res.text)
    title=tree.xpath('//span[@class="title"][1]/text()')
    return title

def get_all_page(start,end):
    result=[]
    for i in range(start,end-start):
        title_list=get_page(i*25)
        result+=title_list

    return result

if __name__=="__main__":
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='scraping',charset="utf8")
    cur=conn.cursor()
    result=get_all_page(0,10)
    for i in range(len(result)):
        cur.execute("insert into blog_movie(name) values('"+result[i]+"')")
    cur.close()
    conn.commit()
    conn.close()