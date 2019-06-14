# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv

class DbmoviePipeline(object):
    def __init__(self):
            # csv文件的位置,无需事先创建
        store_file = "D:\\xx\\爬虫\\实验\\dzy\\scrapy\\DBmovie\\movies.csv"
        print("***************************************************************")
            # 打开(创建)文件
        self.file=open(store_file,'a+',encoding='utf-8',newline='')
            # csv写法
        self.writer = csv.writer(self.file, dialect="excel")

    def process_item(self, item, spider):
            # 判断字段值不为空再写入文件
        print("正在写入......")
        if item['ranking']:
                # 主要是解决存入csv文件时出现的每一个字以‘，’隔离
            self.writer.writerow([item['ranking'],item['movie_name'],item['score']])
        return item

    def close_spider(self, spider):
            # 关闭爬虫时顺便将文件保存退出
        self.file.close()
