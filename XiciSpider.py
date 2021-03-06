# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class XicispiderSpider(scrapy.Spider):
    name = 'xiciSpider'
    allowed_domains = ['xicidaili.com']
    start_urls = []
    wds = ['nn','nt','wn','wt']
    pages = 10
    for type in wds:
        for i in range(1,pages + 1):
            start_urls.append('http://www.xicidaili.com/' + type + '/' + str(i))

    def parse(self, response):
        subs = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        items = []
        for sub in subs:
            item = GetproxyItem()
            item['ip'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['port'] = sub.xpath('.//td[3]/text()').extract()[0]
            #item['type'] = sub.xpath('.//td[5]/text()').extract()[0]
            #if sub.xpath('.//td[4]/a/text()'):
            #    item['loction'] = sub.xpath('//td[4]/a/text()').extract()[0]
            #else:
            #    item['loction'] = sub.xpath('.//td[4]/text()').extract()[0]
            item['protocol'] = sub.xpath('.//td[6]/text()').extract()[0]
            #item['source'] = 'xicidaili'
            items.append(item)
        return items