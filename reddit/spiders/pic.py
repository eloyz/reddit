# -*- coding: utf-8 -*-
import random
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from reddit.items import PicItem

class PicSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['http://www.reddit.com/r/pics/']

    rules = [
    	Rule(LinkExtractor(
    		allow=['/r/pics/\?count=\d*&after=\w*']),
    		callback='parse_item',
    		follow=True)
    ]

    # rules = [
    #     # Traverse the in the /r/pics subreddit. When you don't pass
    #     # callback then follow=True by default.
    #     # It's also important to NOT override the parse method
    #     # the parse method is used by the CrawlSpider continuously extract links
    #     Rule(LinkExtractor(
    #     	allow=['/r/pics/\?count=\d*&after=\w*']),
    #     	callback='parse_item',
    #     	follow=True),
    # ]

    def parse_item(self, response):
        
        selector_list = response.css('div.thing')

        for selector in selector_list:
        	item = PicItem()
        	item['image_urls'] = selector.xpath('a/@href').extract()
        	item['title'] = selector.xpath('div/p/a/text()').extract()
        	item['url'] = selector.xpath('a/@href').extract()

        	yield item
