import scrapy

class QuotesSpider(scrapy.Spider):
    name = "ipadbooks"
    start_urls = [
        'https://bbs.feng.com/thread-htm-fid-224-page-2.html',
    ]

    def parse(self, response):
        for li in response.xpath("//tbody[starts-with(@id,'normalthread_')]/tr/th"):
            aa = li.xpath('a/text()')
            href = li.xpath('a/@href')
            print(aa.extract()[0])
            print(href.extract()[0])
            # for a in aa:
            #     print(a.extract_first())
            #     print("\n")
        print("Game Over")
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)