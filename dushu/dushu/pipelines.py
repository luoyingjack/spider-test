# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DushuPipeline(object):

    def __init__(self):
        self.sql = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='dbbook',charset = 'utf8')
        self.cursor = self.sql.cursor()

        pass

    def process_item(self, item, spider):
        sql = "INSERT INTO book2(book_url,book_title,book_author,book_info) VALUES('%s','%s','%s','%s')"%(item['book_url'],item['book_title'],item['book_author'],item['book_info'])
        flag = self.cursor.execute(sql)
        print('********************************************',flag)
        self.sql.commit()
        return item

    def close_spider(self,spider):

        self.cursor.close()
        self.sql.close()
        pass