# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DocumentItem(scrapy.Item):
    title = scrapy.Field()
    file = scrapy.Field()
    release = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()


class SoftwareItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
