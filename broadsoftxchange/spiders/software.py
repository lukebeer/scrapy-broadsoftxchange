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
        headers = response.headers
        self.log(headers)
        if headers['Content-Type'] != 'text/plain':
            self.log(response.url, level=scrapy.log.INFO)
            if not settings.DOWNLOAD_DRYRUN:
                yield SoftwareItem(file_urls=[response.url])
        if headers['Content-Type'] == 'text/plain':
            if 'Contents of this Folder:' in response.body:
                for link in response.body.split('\n')[1:-1]:
                    url = '%s/%s' % (response.url, link.strip())
                    self.log(url, level=scrapy.log.INFO)
                    yield scrapy.Request(url=url, method=settings.REQUEST_METHOD, callback=self.parse)
            else:
                self.log(response.url, level=scrapy.log.INFO)
                if not settings.DOWNLOAD_DRYRUN:
                    yield SoftwareItem(file_urls=[response.url])
