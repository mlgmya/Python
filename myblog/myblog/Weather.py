from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import MySQLdb

class WeatherDB:
    def openDB(self):
        self.con=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='scraping',charset="utf8")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table blog_weather(wCity varchar(16),wDate varchar(16),wWeather varchar(64),wTemp varchar(32),constraint pk_weather primary key(wCity,wDate))")
        except:
            self.cursor.execute("delete from blog_weather")
    
    def closeDB(self):
        self.con.commit()
        self.con.close()
    
    def insert(self,city,date,weather,temp):
        try:
            self.cursor.execute("insert into blog_weather (wCity,wDate,wWeather,wTemp) values(%s,%s,%s,%s)",(city,date,weather,temp))
        except Exception as err:
            print(err)

    def show(self):
        self.cursor.execute("select * from blog_weather")
        rows=self.cursor.fetchall()
        print("%-16s%-16s%-32s%-16s" % ("city","date","weather","temp"))
        for row in rows:
            print("%-16s%-16s%-32s%-16s" % (row[0],row[1],row[2],row[3]))

class WeatherForecast:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0(Windows;U;Windows NT 6.0 x64;en-US;rv:1.9pre)Gecko/2008072421 Minefield/3.0.2pre"}
        self.cityCode={"北京":"101010100","上海":"101020100","广州":"101280101","温州":"101210701"}

    def forecastCity(self,city):
        if city not in self.cityCode.keys():
            print(city+"code cannot be found")
            return
        url="http://www.weather.com.cn/weather/"+self.cityCode[city]+".shtml"
        try:
            req=urllib.request.Request(url,headers=self.headers)
            data=urllib.request.urlopen(req)
            data=data.read()
            dammit=UnicodeDammit(data,["utf-8","gbk"])
            data=dammit.unicode_markup
            soup=BeautifulSoup(data,"lxml")
            lis=soup.select("ul[class='t clearfix'] li")
            for li in lis:
                try:
                    date=li.select('h1')[0].text
                    weather=li.select('p[class="wea"]')[0].text
                    temp=li.select('p[class="tem"] span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
                    print(city,date,weather,temp)
                    self.db.insert(city,date,weather,temp)
                except Exception as err:
                    print(err)
        except Exception as err:
            print(err)
        
    def process(self,cities):
        self.db=WeatherDB()
        self.db.openDB()

        for city in cities:
            self.forecastCity(city)

        #self.db.show()
        self.db.closeDB()

ws=WeatherForecast()
ws.process(["北京","上海","广州","温州"])
print("completed")

                


