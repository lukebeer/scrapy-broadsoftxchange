# -*- coding: utf-8 -*-
import scrapy


class DocumentItem(scrapy.Item):
    title = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    release = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()


class SoftwareItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
