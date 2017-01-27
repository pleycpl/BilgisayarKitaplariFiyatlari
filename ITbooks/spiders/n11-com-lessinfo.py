import scrapy
# scrapy crawl n11.com out-n11-less.json

class N11Spider(scrapy.Spider):
    name = 'n11.com-lessinfo'
    allowed_domains = ['n11.com']
    start_urls = [
        'http://www.n11.com/kitap/egitim/bilgisayar-kitaplari'
    ]

    def parse(self, response):
        items = response.css('.columnContent')
        for item in items:
            url = item.css('.plink::attr(href)').extract_first()
            if url is None:
                continue
            title = item.css('.plink::attr(title)').extract_first()
            img = item.css('.lazy::attr(data-original)').extract_first()
            old_price = item.css('.oldPrice').xpath('.//del/text()').extract_first()
            price = item.css('.newPrice').xpath('.//text()').extract_first()
            saller = item.css('.sallerInfo::attr(title)').extract_first()

            yield {
                'url':url,
                'title': title,
                'img': img,
                'oldPrice': old_price,
                'price': price,
                'saller': saller,
            }
