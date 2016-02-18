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
        if settings.DOWNLOAD_DRYRUN is not False:
            msg = "DRYRUN: %s" % response.url
        else:
            msg = response.url
        if response.headers['Content-Type'] == 'text/plain':
            if 'Contents of this Folder:' in response.body:
                for link in response.body.split('\n')[1:-1]:
                    next = '%s/%s' % (response.url, link.strip())
                    if settings.BROADWORKS_RELEASE:
                        if settings.BROADWORKS_RELEASE in next:
                            yield scrapy.Request(url=next, method=settings.REQUEST_METHOD, callback=self.parse)
                    else:
                        yield scrapy.Request(url=next, method=settings.REQUEST_METHOD, callback=self.parse)
        elif not settings.DOWNLOAD_DRYRUN and settings.BROADWORKS_ARCH in response.url:
           if settings.BROADWORKS_RELEASE:
               if settings.BROADWORKS_RELEASE in response.url:
                   self.log(msg, level=scrapy.log.INFO)
                   yield SoftwareItem(file_urls=[response.url])
           else:
               self.log(msg, level=scrapy.log.INFO)
               yield SoftwareItem(file_urls=[response.url])