# scrapy-broadsoftxchange
Crawler and downloader for Broadsoft's xchange to provide a local software and document collection.

The software/doc bundles on xchange don't include everything and it's a pain to manually download.

I personally use this to populate a documentation indexing and text mining engine for snappy searching.

PyPI: https://pypi.python.org/pypi/scrapy-broadsoftxchange


##### Install directly from PyPI
```
bash-$ pip install scrapy-broadsoftxchange
```

##### Install from Github
```
bash-$ pip install scrapy
bash-$ git clone https://github.com/lukebeer/scrapy-broadsoftxchange.git
bash-$ cd scrapy-broadsoftxchange
```

##### Usage

If you installed from PyPi rather than a local cloned copy, you need to set SCRAPY_SETTINGS_MODULE
```
bash-$ export SCRAPY_SETTINGS_MODULE=broadsoftxchange.settings
```
You can edit settings.py to include your credentials but it's much faster to just export vars as per below:
``` 
bash-$ export XCHANGE_USERNAME='user@example.com'
bash-$ export XCHANGE_PASSWORD='password'
```

##### Optional
The default setting stores files in the users home dir. To change, set XCHANGE_STORE to the new location.
```
bash-$ export XCHANGE_STORE='/data/documents'
```

Start the download for 'documentation' or 'software'
```
bash-$ scrapy crawl documentation
2015-09-20 15:20:29 INFO: Scrapy 1.0.3 started (bot: scrapy-broadsoftxchange)
2015-09-20 15:20:29 INFO: Optional features available: ssl, http11
2015-09-20 15:20:29 INFO: Overridden settings: {'DOWNLOAD_TIMEOUT': 1800, 'REDIRECT_MAX_TIMES': 70, 'LOG_LEVEL': 'INFO', 'CONCURRENT_REQUESTS_PER_DOMAIN': 16, 'RANDOMIZE_DOWNLOAD_DELAY': False, 'DOWNLOAD_WARNSIZE': 1073741824, 'SPIDER_MODULES': ['broadsoftxchange.spiders'], 'LOG_STDOUT': True, 'CONCURRENT_REQUESTS_PER_IP': 16, 'BOT_NAME': 'scrapy-broadsoftxchange', 'DOWNLOAD_MAXSIZE': 4294967296, 'CONCURRENT_ITEMS': 32, 'RETRY_TIMES': 10, 'REACTOR_THREADPOOL_MAXSIZE': 16, 'TELNETCONSOLE_ENABLED': False, 'LOG_FORMAT': '%(asctime)s %(levelname)s: %(message)s', 'MEMUSAGE_ENABLED': True, 'USER_AGENT': 'scrapy-broadsoftxchange (+https://github.com/lukebeer/scrapy-broadsoftxchange)'}
2015-09-20 15:20:29 INFO: Enabled extensions: CloseSpider, MemoryUsage, LogStats, SpiderState, AutoThrottle, CoreStats
2015-09-20 15:20:29 INFO: Enabled downloader middlewares: HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, ChunkedTransferMiddleware, DownloaderStats
2015-09-20 15:20:29 INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
2015-09-20 15:20:29 INFO: Enabled item pipelines: PathPipeline
2015-09-20 15:20:29 INFO: Spider opened
2015-09-20 15:20:29 INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2015-09-20 15:20:44 INFO: BroadWorks Performance Measurement Interface Specification
2015-09-20 15:20:44 INFO: BW-Assistant-Enterprise-ReleaseNotes-R17.SP4 MB16
2015-09-20 15:20:44 INFO: BW-Assistant-Enterprise-ReleaseNotes-R18 MB15
2015-09-20 15:20:44 INFO: Rel19.sp4_XsiCTISchema_389176
2015-09-20 15:20:44 INFO: BroadSoft Partner Configuration Guide Polycom RealPresence Mobile
2015-09-20 15:20:44 INFO: BW-Assistant-Enterprise-ReleaseNotes-R17 SP4 MB17
2015-09-20 15:20:44 INFO: BW Thin Call Center Release Notes 17.2.132
2015-09-20 15:20:44 INFO: BW Thin Receptionist Release Notes 17.2.136
2015-09-20 15:20:44 INFO: Rel_19.sp1_BW-Accounting-CDR-Files
2015-09-20 15:20:44 INFO: BW Thin Call Center Release Notes 19.0.20
2015-09-20 15:20:44 INFO: BW Thin Receptionist Release Notes 19.0.17
2015-09-20 15:20:44 INFO: Support Newsletter April 2013
2015-09-20 15:20:44 INFO: Rel_19.sp1_1.574_OCISchema_ALL_392340
2015-09-20 15:20:44 INFO: Rel_19.sp1_1.574_OCISchema_AS_HTML_392340
2015-09-20 15:20:44 INFO: Network_Server_Lesson_1_Introduction
2015-09-20 15:20:44 INFO: Network_Server_Lesson_2_Policies_and_Profiles
2015-09-20 15:20:44 INFO: BroadWorks Accounting Call Detail Record Interface Specification
2015-09-20 15:20:44 INFO: BroadWorks Accounting Call Detail Record Interface Specification
2015-09-20 15:20:44 INFO: Network_Server_Lesson_4 _NDC_and_Call_Screening
2015-09-20 15:20:44 INFO: NS_Lesson_5_On_Network_Routing
2015-09-20 15:20:44 INFO: Network_Server_Lesson_3_Dial_Plans_and_Call_Typing
2015-09-20 15:20:44 INFO: Calling Party Address Strict Compliance Feature Description
2015-09-20 15:20:44 INFO: BroadWorks Service Interaction Guide
...
2015-09-20 15:21:25 INFO: Crawled 40 pages (at 40 pages/min), scraped 29 items (at 29 items/min)
2015-09-20 15:22:49 INFO: Crawled 68 pages (at 28 pages/min), scraped 57 items (at 28 items/min)
