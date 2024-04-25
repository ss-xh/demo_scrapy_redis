import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from ..items import DemoScrapyRedisItem


class DemoSpider(RedisSpider):
    name = "demo"
    base_url = "https://pic.netbian.com"

    # redis数据库通过设置 set demo_start_url "https://demo.com" 添加起始url
    # https://pic.netbian.com/4kmeinv/
    redis_key = "demo:start_url"

    def parse(self, response):
        response.body.decode("gbk")
        image_links = re.findall(r'<a href="(/tupian/.*?html)" target', response.text)
        for image_link in image_links:
            # 图片详情页地址
            yield scrapy.Request(DemoSpider.base_url + image_link, callback=self.parse_detail)

        # 下一页地址
        if re.search(r"下一页", response.text):
            next_url = response.xpath('//div[@class="page"]/a[last()]/@href').extract_first()
            yield scrapy.Request(DemoSpider.base_url + next_url, callback=self.parse)

    def parse_detail(self, response):
        response.body.decode("gbk")
        item = DemoScrapyRedisItem()
        item["src"] = DemoSpider.base_url + response.xpath('//a[@id="img"]/img/@src').extract_first()
        item["title"] = response.xpath('//a[@id="img"]/img/@title').extract_first()
        yield item
