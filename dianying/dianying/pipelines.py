# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class DianyingPipeline(object):

    def __init__(self):
        self.sql = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='dbmovie',charset = 'utf8')
        self.cursor = self.sql.cursor()

        pass

    def process_item(self, item, spider):
        sql = "INSERT INTO movie(movie_title,movie_class,movie_info,movie_date,movie_post_url,movie_download_url) VALUES('%s','%s','%s','%s','%s','%s')"%(item['movie_title'],item['movie_class'],item['movie_info'],item['movie_date'],item['movie_post_url'],item['movie_download_url'])
        flag = self.cursor.execute(sql)
        print('********************************************',flag)
        self.sql.commit()
        return item

    def close_spider(self,spider):

        self.cursor.close()
        self.sql.close()
        pass