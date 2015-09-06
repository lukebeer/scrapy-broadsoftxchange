# -*- coding: utf-8 -*-
import scrapy
from scrapy import spiders, log

from broadsoftxchange.items import SoftwareItem
from broadsoftxchange import settings


class SoftwareSpider(spiders.CrawlSpider):
    name = "software"
    http_user = settings.XCHANGE_USERNAME
    http_pass = settings.XCHANGE_PASSWORD
    start_urls = [
        'http://xchange.broadsoft.com/XchangeRepos/GA',
    ]

    def parse(self, response):
        self.log(response.url, level=scrapy.log.INFO)
        if response.headers['Content-Type'] != 'text/plain':
            if not settings.DOWNLOAD_DRYRUN:
                yield SoftwareItem(file_urls=[response.url])
        else:
            if 'Contents of this Folder:' in response.body:
                for link in response.body.split('\n')[1:-1]:
                    next = '%s/%s' % (response.url, link.strip())
                    yield scrapy.Request(url=next, method=settings.REQUEST_METHOD, callback=self.parse)
            else:
                self.log(response.url, level=scrapy.log.INFO)
                if not settings.DOWNLOAD_DRYRUN:
                    yield SoftwareItem(file_urls=[response.url])
