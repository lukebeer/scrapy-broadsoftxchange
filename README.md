# scrapy-broadsoftxchange
Crawler and downloader for Broadsoft's xchange to provide a local software and document collection.

#### Nutshell
```
bash-$ pip install scrapy
bash-$ git clone https://github.com/lukebeer/scrapy-broadsoftxchange.git
```
*set username & password in broadsoftxchange/settings.py*
```
bash-$ scrapy crawl [software, documents]
```

#### Settings
*broadsoftxchange/settings.py*
```
XCHANGE_USERNAME = 'username@example.com'
XCHANGE_PASSWORD = 'password'
LOG_ENABLED = True
LOG_FILE = None
LOG_FORMAT = '%(message)s'  #  '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_LEVEL = 'INFO'
LOG_STDOUT = True
DEPTH_STATS = False
DEPTH_STATS_VERBOSE = False
DOWNLOADER_STATS = True
MEMDEBUG_ENABLED = False
MEMUSAGE_ENABLED = False
MEMUSAGE_LIMIT_MB = 0
AUTOTHROTTLE_DEBUG = False
TELNETCONSOLE_ENABLED = False
DOWNLOAD_TIMEOUT = 1800
DOWNLOAD_MAXSIZE = 4294967296  # 4GB
DOWNLOAD_WARNSIZE = 1073741824  # 1GB
DOWNLOAD_DRYRUN = True
FILES_STORE = os.path.expanduser('~')
REQUEST_METHOD = 'HEAD'
RETRY_ENABLED = True
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408]
```
