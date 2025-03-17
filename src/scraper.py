import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://hadits.in/bukhari/"+str(i) for i in range(1,7009)
    ]

    def parse(self, response):
        title = response.css("title::text").get()
        yield {
            "Nomor": title[15:].split(" tentang '")[0],
            "Kitab": title[15:].split(" tentang '")[1].split(": ",1)[0],
            "Bab": title[15:].split(" tentang '")[1].split(": ",1)[1],
            "indo": response.xpath("//meta[@name='description']/@content").extract(),
        }