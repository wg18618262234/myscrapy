# -*- coding: utf-8 -*-
import scrapy
import sys

sys.path.append('..')
from myscrapyspider.items import ItcastItems as IT


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        items = []

        for each in response.xpath('//div[@class="li_txt"]'):
            item = IT()

            name = each.xpath('h3/text()').extract()
            titile = each.xpath('h4/text()').extract()
            info = each.xpath('p/text()').extract()

            item['name'] = name[0]
            item['title'] = titile[0]
            item['info'] = info[0]

            items.append(item)

        return items
        pass
