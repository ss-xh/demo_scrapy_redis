from scrapy.cmdline import execute


def main():
    execute(['scrapy', 'crawl', 'demo'])


if __name__ == "__main__":
    main()
