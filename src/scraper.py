import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.hadits.id/hadits/bukhari/"+str(i) for i in range(1,7009)
    ]

    def parse(self, response):
        title = response.css("div.hadits-about")
        content = response.css("article.hadits-content")
        yield {
            "Nomor": title.css("h2::text").get()[29:].split(" - ",1)[0],
            "Bab": title.css("h2::text").get()[29:].split(" - ",1)[1],
            "Tentang": content.css("h1::text").get(),
            "Terjemahan": content.css("a.copy-btn").attrib["data-string"].split(" https://")[0],
        }