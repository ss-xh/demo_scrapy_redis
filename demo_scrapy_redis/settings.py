SPIDER_MODULES = ["demo_scrapy_redis.spiders"]
NEWSPIDER_MODULE = "demo_scrapy_redis.spiders"

# CONCURRENT_REQUESTS = 32

# DOWNLOAD_DELAY = 1
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# COOKIES_ENABLED = False

# TELNETCONSOLE_ENABLED = False

# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# SPIDER_MIDDLEWARES = {
#    "demo_scrapy_redis.middlewares.DemoScrapyRedisSpiderMiddleware": 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#    "demo_scrapy_redis.middlewares.DemoScrapyRedisDownloaderMiddleware": 543,
# }

# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# ITEM_PIPELINES = {
#    "demo_scrapy_redis.pipelines.DemoScrapyRedisPipeline": 300,
# }

# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 关闭君子协议
ROBOTSTXT_OBEY = False

# 设置日志显示级别
LOG_LEVEL = "ERROR"

# 设置全局默认ua
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

# 设置每个请求最大等待时长
DOWNLOAD_TIMEOUT = 3

# scrapy_redis 支持的第三方管道类,支持多机器数据共享
ITEM_PIPELINES = {
    "demo_scrapy_redis.pipelines.DemoScrapyRedisPipeline": 200,
    "scrapy_redis.pipelines.RedisPipeline": 300,
}

# 1.启用调度将请求存储进redis
# CHEDULER = "scrapy_redis.scheduler.Scheduler"

# 2.确保所有spider通过redis共享相同的重复过滤。
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 使用布隆过滤器对应的规则 pip install scrapy-redis-bloomfilter
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
BLOOMFILTER_HASH_NUMBER = 6
BLOOMFILTER_BIT = 30

# 3.队列中的内容是否持久保存，为False的时候会在关闭redis的时候清空redis,类似断点续传的功能
SCHEDULER_PERSIST = True

# 4.指定redis数据库的地址 (关闭redis.conf配置文件的只允许本机访问, 保护模式)
# REDIS_URL = 'redis://192.168.10.150:6379'
REDIS_HOST = "192.168.10.254"
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
REDIS_PARAMS = {"password": "root"}
