# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import DushuItem
class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1175.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1175_\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        books = response.xpath('//div[@class="bookslist"]/ul/li')

        for book in books:
            item = DushuItem()
            book_url = book.xpath('.//div[contains(@class,"img")]/a/img/@src').extract_first()
            book_title = book.xpath('.//a/@title').extract_first()
            book_info = book.xpath('.//p[@class="disc eps"]/text()').extract_first()
            book_author = book.xpath('.//p[1]/a/text()').extract_first(default='佚名')

            item['book_url'] = book_url
            item['book_title'] = book_title
            item['book_info'] = book_info
            item['book_author'] = book_author
            yield item
