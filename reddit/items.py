# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PicItem(Item):
    image_urls = Field()
    images = Field()
    title = Field()
    url = Field()

# class ShowerThoughtItem(Item):
#     image_urls = Field()
#     images = Field()
#     title = Field()
#     url = Field()