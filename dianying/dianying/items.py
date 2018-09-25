# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianyingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_title = scrapy.Field()
    movie_class = scrapy.Field()
    movie_info = scrapy.Field()
    movie_date = scrapy.Field()
    movie_post_url = scrapy.Field()
    movie_download_url = scrapy.Field()

