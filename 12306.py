from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
import numpy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import re

def init_browser(b):
    b.maximize_window()

def visit_login_page(b):
    url = 'https://kyfw.12306.cn/otn/resources/login.html'
    b.get(url)
    time.sleep(2)
    b.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
    time.sleep(2)     #访问login page后休息2秒，等待验证码图片加载完成 

def try_login(b):
    for k in range(0,5):     #连续尝试5次
        rt_val=login(b)
        if rt_val < 0:     
            print("验证码错误")
            time.sleep(10)
            continue
        elif rt_val == 1:   
            print("刷新验证码")
            time.sleep(5)
            continue     
        else:      
            return 0   
        return -1  

def login(b):
    pic_name=None
    try:
        username=b.find_element_by_id('J-userName')
        username.clear()
        username.send_keys('18758622377')
        password=b.find_element_by_id('J-password')
        password.clear()
        password.send_keys('78965223ying') 
        time.sleep(2) 
        pic_name=get_a_verify_pic(b)   #截取12306验证码图片
        body_list=ana_pic(b,pic_name) #破解12306验证码
        if len(body_list) == 0:    #没有图片
            click_refresh(b)
            print("login : what??? body list is null!!!")
            os.remove(pic_name)   
            return 1   
        num = b.window_handles
        b.switch_to.window(num[0])
        click_pic(b,body_list)
        time.sleep(1)      #休息1秒再点击登陆按钮
        b.find_element_by_xpath("//*[@id='J-login']").click()
    except:
        if None != pic_name:
            os.remove(pic_name)   
        return -1
    time.sleep(5)   
    os.remove(pic_name)
    return 0

def get_a_verify_pic(b):
    img_element =WebDriverWait(b, 100).until(EC.presence_of_element_located((By.ID, "J-loginImg")))
    str=img_element.get_attribute("src").split(",")[-1]
    imgdata=base64.b64decode(str)
    pic_name="verify_code.jpg"
    with open("verify_code.jpg",'wb') as file:
	    file.write(imgdata)
    return pic_name

#破解图片验证码
def ana_pic(b,pic_name):
    js='window.open("http://littlebigluo.qicp.net:47720/");'
    b.execute_script(js)
    num = b.window_handles
    b.switch_to.window(num[1])
    time.sleep(2) 
    body_list=[]
    imgPath="D:\\xx\\爬虫\\实验\\dzy\\verify_code.jpg"
    b.find_element_by_xpath('/html/body/form/input[1]').send_keys(imgPath)
    b.find_element_by_xpath('/html/body/form/input[2]').click()
    ans=b.find_element_by_xpath('/html/body/p[1]/font/font/b').text
    s=ans.split()   
    for index in s:
        body_list.append(int(index))
        print(body_list)
    time.sleep(2)
    b.close()
    return body_list

def click_pic(b,body_list):
    for i in range(len(body_list)):
        click_one_pic(b,body_list[i])
        print(body_list[i])
        time.sleep(1)

def click_refresh(b):
    try:
        b.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[3]").click()
    except:
        print("刷新失败")

def click_one_pic(b,i):
    try:
        imgelement=b.find_element_by_xpath("//*[@id='J-loginImg']")
        if i<=4:
            ActionChains(b).move_to_element_with_offset(imgelement,40+72*(i-1),73).click().perform()
        else:
            i -= 4
            ActionChains(b).move_to_element_with_offset(imgelement,40+72*(i-1),145).click().perform()
    except:
        print("点击失败")

def click_button(b,id,dest_text,j):  #在当前页面查找并点击指定text，错误返回 -1.连续5次，错误时延时1秒
    txt=''
    for i in range(0,5):
        try:
            txt=b.find_element_by_id(id).text
            if txt == dest_text:
                b.find_element_by_id(id).click()
                return 0
            else:
                return 1
        except:
            time.sleep(1)
            continue
        return -1       #5次都失败了

if __name__ == "__main__": 
    b = webdriver.Firefox()
    init_browser(b)
    visit_login_page(b)
    ret_val = try_login(b) #尝试登录
    if ret_val<0:  
        print("登录失败") 
    else:
        print("登录成功") 
    print("complete")
