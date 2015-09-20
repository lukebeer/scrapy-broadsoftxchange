# -*- coding: utf-8 -*-
import logging

import scrapy
from scrapy import spiders, linkextractors
from scrapy.selector import Selector

from broadsoftxchange.items import DocumentItem


class Documentation(spiders.CrawlSpider):
    name = 'documentation'
    allowed_domains = ['xchange.broadsoft.com']
    login_page = 'http://xchange.broadsoft.com/php/xchange/'
    start_urls = ['http://xchange.broadsoft.com/php/xchange/support/broadworks/documentation?page=1']
    rules = (
        spiders.Rule(
            linkextractors.LinkExtractor(allow=r'/php/xchange/support/broadworks/documentation\?page=[0-9]+',
                                         unique=True, canonicalize=False),
            callback='parse_item',
            follow=True,
        ),
    )

    def start_requests(self):
        yield scrapy.Request(
            url=self.login_page,
            callback=self.login,
            dont_filter=False,
        )

    def login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formxpath='//*[@id="user-login-form"]',
            formdata={
                'name': self.settings['XCHANGE_USERNAME'],
                'pass': self.settings['XCHANGE_PASSWORD']
            },
            callback=self.check_login_response,
        )

    def check_login_response(self, response):
        try:
            if 'Configure your rss feeds' in response.body:
                self.log("Successfully logged in")
                for url in self.start_urls:
                    yield scrapy.Request(url=url)
        except:
            self.log("Login failed")
            return

    def parse_item(self, response):
        items = []
        hxs = Selector(response)
        links = hxs.xpath("//tr[@class='odd rowclick even']|//tr[@class='even rowclick odd']")
        for row in links:
            item = DocumentItem()
            item['title'] = row.xpath("./td[3]/a/text()").extract() or ['']
            item['file_urls'] = row.xpath("td[2]/a/@href").extract() or None
            item['release'] = row.xpath("td[6]/text()").extract() or ''
            item['category'] = row.xpath("td[5]/text()").extract() or ''
            item['date'] = row.xpath('td[7]/text()').extract() or ''
            if not item['file_urls']:
                continue
            self.log(item['title'][0], logging.INFO)
            items.append(item)
        return items
