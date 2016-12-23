# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Spider,Rule
from scrapy.linkextractors import LinkExtractor
from ChineseRegion.items import ChineseregionItem


class RegionSpider(Spider):
    name = "region"
    #allowed_domains = ["http://www.stats.gov.cn"]
    start_urls = [
        "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html",
    ]
    # rules = [
    #     Rule(LinkExtractor(allow=(r'\d+\.html')), 'parse_item')
    # ]

    def parse_item(self, response):
        print response.body

    def parse(self, response):
        for links in response.css('.provincetr td a'):
            item = ChineseregionItem()
            item['code'] = links.xpath('@href').extract()[0].rstrip('.html')
            item['name'] = links.xpath('text()').extract()[0]
            item['pcode'] = ''
            yield item
