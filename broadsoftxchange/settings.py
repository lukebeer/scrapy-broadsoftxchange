# -*- coding: utf-8 -*-
import os


#  User configuration & settings
XCHANGE_USERNAME = os.getenv('XCHANGE_USER', 'username@example.com')
XCHANGE_PASSWORD = os.getenv('XCHANGE_PASS', 'password')
LOG_ENABLED = True
LOG_FILE = None
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
LOG_LEVEL = 'INFO'
LOG_STDOUT = True
DEPTH_STATS = True 
DEPTH_STATS_VERBOSE = False
DOWNLOADER_STATS = True
MEMDEBUG_ENABLED = False
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 0
AUTOTHROTTLE_DEBUG = False
TELNETCONSOLE_ENABLED = False
DOWNLOAD_TIMEOUT = 1800
DOWNLOAD_MAXSIZE = 4294967296  # 4GB
DOWNLOAD_WARNSIZE = 1073741824  # 1GB
DOWNLOAD_DRYRUN = False
FILES_STORE = os.path.join(os.getenv('XCHANGE_STORE', os.path.expanduser('~')), 'Broadsoft')
REQUEST_METHOD = 'GET'
RETRY_ENABLED = True
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408]


#  Optimized defaults for best performance & kindness to xchange.
BOT_NAME = 'scrapy-broadsoftxchange'
USER_AGENT = 'scrapy-broadsoftxchange (+https://github.com/lukebeer/scrapy-broadsoftxchange)'
SPIDER_MODULES = ['broadsoftxchange.spiders']
EXTENSIONS = {'scrapy.extensions.corestats.CoreStats': 500}
ITEM_PIPELINES = {'broadsoftxchange.pipelines.PathPipeline': 1}
RANDOMIZE_DOWNLOAD_DELAY = False
REACTOR_THREADPOOL_MAXSIZE = 16
REDIRECT_MAX_TIMES = 70 
CONCURRENT_REQUESTS = 16
CONCURRENT_ITEMS = 32 
DEPTH_LIMIT = 0
DEPTH_PRIORITY = 0
DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
COOKIES_ENABLED = True
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
