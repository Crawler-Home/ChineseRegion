# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ChineseRegion.items import ChineseregionItem


class RegionSpider(CrawlSpider):
    name = "region"
    allowed_domains = ["stats.gov.cn"]
    start_urls = [
        "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html",
    ]
    rules = [
        Rule(LinkExtractor( allow=(r'\d+\.html')), callback='parse_item', follow=False )
    ]

    def parse_item(self, response):
        print '***************' + response.url + '****************************'
        for links in response.css('.provincetr td a'):
            print links.xpath('@href').extract()[0].rstrip('.html')
            print links.xpath('text()').extract()[0]
            # item = ChineseregionItem()
            # item['code'] = links.xpath('@href').extract()[0].rstrip('.html')
            # item['name'] = links.xpath('text()').extract()[0]
            # item['pcode'] = ''
            # yield item

        for city in response.css('.citytr'):
            print city.xpath('td[1]/a/text()').extract()[0]
            print city.xpath('td[2]/a/text()').extract()[0]

        for county in response.css('.countytr'):
            print county.xpath('td[1]/a/text()').extract()[0]
            print county.xpath('td[2]/a/text()').extract()[0]