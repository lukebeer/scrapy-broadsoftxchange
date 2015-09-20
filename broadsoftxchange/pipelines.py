# -*- coding: utf-8 -*-
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


class PathPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        bits = urlparse(url)
        path = bits.netloc + bits.path
        if path.startswith('xchange.broadsoft.com/php/xchange/system/files/'):
            return path.strip('xchange.broadsoft.com/php/xchange/system/files/')
        return path
