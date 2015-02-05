# -*- coding: utf-8 -*-

# Scrapy settings for reddit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'reddit'

SPIDER_MODULES = ['reddit.spiders']
NEWSPIDER_MODULE = 'reddit.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'reddit (+http://www.yourdomain.com)'

FEED_URI = 'logs/%(name)s/%(time)s.csv'
FEED_FORMAT = 'csv'

IMAGES_STORE = 'images/'
IMAGES_EXPIRES = 90  # 90 days of delay for image expiration


ITEM_PIPELINES = {
	'scrapy.contrib.pipeline.images.ImagesPipeline': 99,
	'reddit.pipelines.RedditPipeline': 100,
}

