# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.misc import md5sum
import os


class SoftwarePipeline(FilesPipeline):
    def file_downloaded(self, response, request, info):
        path = self.file_path(request, response=response, info=info)
        buf = BytesIO(response.body)
        self.store.persist_file(path, buf, info)
        return os.path.basename(path)
