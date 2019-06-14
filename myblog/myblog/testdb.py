# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Movie,Weather
 
# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Weather.objects.all()
    # 输出所有数据
    for var in list:
        response1 += var.wCity+ var.wDate+var.wWeather+var.wTemp+ " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

    