from django.contrib import admin
from django.conf.urls import url
from . import views


app_name='blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^movie/$',views.movie,name='movie'),
    url(r'^weather/$', views.weather, name='weather'),
    url(r'^phones/$', views.phones, name='phones'),
    url(r'^bags/$', views.bags, name='bags'),
    url(r'^info/$', views.info, name='info'),
]