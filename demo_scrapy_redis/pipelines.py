import socket


class DemoScrapyRedisPipeline:
    def open_spider(self, spider):
        self.host_ip = socket.gethostbyname(socket.gethostname())

    def process_item(self, item, spider):
        print(f"当前主机ip:{self.host_ip} -> 爬取到的数据是:{item}")
        return item
