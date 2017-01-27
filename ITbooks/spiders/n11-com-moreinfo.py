import scrapy
# scrapy crawl n11.com-moreinfo -o out-n11-more.json

class N11Spider(scrapy.Spider):
    name = 'n11.com-moreinfo'
    allowed_domains = ['n11.com']
    start_urls = [
        'http://www.n11.com/kitap/egitim/bilgisayar-kitaplari'
    ]

    def parse(self, response):
        items = response.css('.columnContent')
        for item in items:
            url = item.css('.plink::attr(href)').extract_first()
            if url is not None:
                yield scrapy.Request(response.urljoin(url), callback=self.parse_books)

        next_page = response.css('.pagination .next::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_books(self, response):
        proName     = response.css('.proName::text').extract_first().strip()
        proSubName  = response.css('.proSubName::text').extract_first().strip()
        pic         = response.css('.zoom::attr(href)').extract_first()
        oldPrice    = response.css('.oldPrice::text').extract_first().strip()
        newPrice    = response.css('.newPrice ins::text').extract_first().strip()
        #publisher, author, language = response.css('.data span::text').extract()
        content     = response.css('.details').xpath('string(.)').extract_first()
        content     = ' '.join(content.split())
        yield {
            'product_name' : proName + ' ' + proSubName,
            'picture'   : pic,
            #'author'    : author,
            #'publisher' : publisher,
            'newPrice'  : newPrice,
            'oldPrice'  : oldPrice,
            'content'   : content,
        }
