import scrapy
# scrapy crawl dr.com.tr out-less.json
class DrSpider(scrapy.Spider):
    name = 'dr.com.tr-lessinfo'
    allowed_domains = ['dr.com.tr']
    start_urls = [
        'http://www.dr.com.tr/kategori/Kitap/Egitim-Basvuru/Bilgisayar'
    ]

    def parse(self, response):
        items = response.css('.item-name')
        for item in items:
            url = item.css('::attr(href)').extract_first()
            url = url[:-1] # space
            title = item.css('::attr(title)')
            price = item.css('.price::text').extract_first()
            old_price = item.css('.old-price::text').extract_first()
            yield {
                'url': url,
                'title': title,
                'price': price,
                'oldPrice': old_price,
            }
