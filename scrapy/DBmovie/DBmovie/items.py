# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy

class DoubanMovieItem(scrapy.Item):
    ranking = scrapy.Field()        #排名
    movie_name = scrapy.Field()     #电影名称
    score = scrapy.Field()          #评分