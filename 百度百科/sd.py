import requests
import re
import time

time1=time.time()
exist_url=[]
g_writecount=0

def scrappy(url,depth=1):
    global g_writecount
    try:
        headers={"User-Agent":"Mozilla/5.0(Windows;U;Windows NT 6.0 x64;en-US;rv:1.9pre)Gecko/2008072421 Minefield/3.0.2pre"}
        r=requests.get("https://baike.baidu.com/"+url,headers=headers)
        html=r.content.decode("utf-8")
    except Exception as e:
        print('Failed downloading and saving',url)
        print(e)
        exist_url.append(url)
        return None

    exist_url.append(url)
    link_list=re.findall('<a href="/fenlei/([^:#=<>]*?)".*?</a>',html)
    unique_list=list(set(link_list)-set(exist_url))

    for eachone in unique_list:
        g_writecount+=1
        output="No."+str(g_writecount)+"\t Depth:"+str(depth)+"\t"+url+'->'+eachone+'\n'
        print(output)
        with open('sd.txt',"a+",encoding='UTF-8') as f:
            f.write(output)
            f.close()
        if depth<2:
            scrappy(eachone,depth+1)
scrappy("")
time2=time.time()
print("Total time",time2-time1)