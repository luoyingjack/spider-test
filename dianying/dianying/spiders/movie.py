# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DianyingItem
class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/china/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'html/gndy/china/list_4_\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        movies = response.xpath('//table[@class="tbspan"]')
        for movie in movies:
            item = DianyingItem()
            movie_title = movie.xpath('.//b/a[2]/text()').extract_first()
            movie_class = movie.xpath('.//b/a[1]/text()').extract_first()
            movie_info = movie.xpath('.//tr[4]/td/text()').extract_first()
            movie_date = movie.xpath('.//font/text()').extract_first()

            # print(movie_title,movie_class,movie_info,movie_date)

            item['movie_title'] = movie_title
            item['movie_class'] = movie_class
            item['movie_info'] = movie_info
            item['movie_date'] = movie_date

            movie_detail_url = 'http://www.ygdy8.net' + movie.xpath('.//a[last()]/@href').extract_first()

            yield scrapy.Request(url=movie_detail_url,callback=self.parse_detail,meta={'item':item})
        # return i

    def parse_detail(self, response):
        item = response.meta['item']

        # 电影海报
        movie_post_url = response.xpath('//img/@src').extract()[1]
        movie_download_url = response.xpath('//td[@bgcolor="#fdfddf"]/a/@href').extract_first()
        print(movie_post_url,movie_download_url,"******************")
        item['movie_post_url'] = movie_post_url
        item['movie_download_url'] = movie_download_url

        yield item