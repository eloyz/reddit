# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
# from reddit.items import ShowerThoughtItem


class ShowerThoughtSpider(CrawlSpider):
    name = "shower_thought"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['http://www.reddit.com/r/Showerthoughts/']

    rules = [
        # Traverse the in the /r/pics subreddit.  We're not extracting data from these
        # pages so there's no need to pass a callback.  When you don't pass
        # callback then follow=True by default.
        # It's also important to NOT override the parse method
        # the parse method is used by the CrawlSpider continuously extract links
        Rule(LinkExtractor(
        	allow=['/r/Showerthoughts/\?count=\d*&after=\w*']),
        	callback='parse_item',
        	follow=True),
    ]

    def parse_item(self, response):
        
        selector_list = response.css('div.thing')

        for selector in selector_list:
        	item = ShowerThoughtItem()
        	item['image_urls'] = selector.xpath('a[contains(@class, "thumbnail")]/@href').extract()
        	item['title'] = selector.xpath('div/p/a/text()').extract()
        	item['url'] = selector.xpath('a/@href').extract()

        	yield item
