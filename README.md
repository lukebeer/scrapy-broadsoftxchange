# scrapy-broadsoftxchange
Crawler and downloader for Broadsoft's xchange to provide a local software and document collection.

PyPI: https://pypi.python.org/pypi/scrapy-broadsoftxchange


##### Install with pip
```
bash-$ pip install scrapy-broadsoftxchange
bash-$ export SCRAPY_SETTINGS_MODULE=broadsoftxchange.settings
```

##### Without pip
```
bash-$ pip install scrapy
bash-$ git clone https://github.com/lukebeer/scrapy-broadsoftxchange.git
bash-$ cd scrapy-broadsoftxchange
```

##### Usage
``` 
bash-$ export XCHANGE_USERNAME='user@example.com'
bash-$ export XCHANGE_PASSWORD='password'
bash-$ scrapy crawl [software, documents]
```
