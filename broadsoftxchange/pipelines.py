# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
from urlparse import urlparse

from scrapy.pipelines.files import FilesPipeline

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from scrapy.http import Request


class SoftwarePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        bits = urlparse(url)
        return bits.netloc + bits.path
