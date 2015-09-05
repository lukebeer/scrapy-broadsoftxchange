# -*- coding: utf-8 -*-
import scrapy
from scrapy import spiders, linkextractors

from broadsoftxchange.items import DocumentItem


class Documentation(spiders.CrawlSpider):
    name = 'documentation'
    allowed_domains = ['xchange.broadsoft.com']
    login_page = 'http://xchange.broadsoft.com/php/xchange/'
    start_urls = ['http://xchange.broadsoft.com/php/xchange/support/broadworks/documentation?page=1']

    rules = (
        spiders.Rule(
            linkextractors.LinkExtractor(allow=r'/php/xchange/support/broadworks/documentation\?page=[0-9]+',
                                         unique=False, canonicalize=False),
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
                    yield scrapy.Request(url=url, dont_filter=True)
        except:
            self.log("Login failed")
            return

    def parse_item(self, response):
        items = []
        links = response.xpath("//tr[@class='odd rowclick even']|//tr[@class='even rowclick odd']")
        for row in links:
            self.log(row)
            item = DocumentItem()
            item['title'] = row.select("td[3]/a/text()").extract()
            item['file'] = row.select("td[2]/a/@href").extract()
            item['release'] = row.select("td[6]/text()").extract()
            item['category'] = row.select("td[5]/text()").extract()
            item['date'] = row.select('td[7]/text()').extract()
            self.log(item)
            items.append(item)
        return items
