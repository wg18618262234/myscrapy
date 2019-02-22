# -*- coding: utf-8 -*-
import scrapy
import sys

sys.path.append('..')
from myscrapyspider.items import JDgoodsItems as JD


class JdgoodsSpider(scrapy.Spider):
    name = 'jdgoods'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E7%8E%A9%E5%85%B7&enc=utf-8&spm=2.1.0']

    def parse(self, response):
        items = []
        # open('jdgoodstest.html', 'wb').write(response.body)
        for each in response.xpath('//li[@class="gl-item"]'):
            item = JD()

            sku = each.xpath('@data-sku').extract()
            name = each.xpath('div/div[3]/a/em/text()').extract()
            price = each.xpath('div/div[2]/strong/i/text()').extract()

            item['sku'] = sku[0]
            item['name'] = name[0]
            item['price'] = price[0]

            items.append(item)

        return items
        pass
