import scrapy
# scrapy crawl dr.com.tr-lessinfo -o out-less.json
class DrSpider(scrapy.Spider):
    name = 'dr.com.tr-lessinfo'
    allowed_domains = ['dr.com.tr']
    start_urls = [
        'http://www.dr.com.tr/kategori/Kitap/Egitim-Basvuru/Bilgisayar'
    ]

    def parse(self, response):
        items = response.css('.content')
        for item in items:
            title = item.xpath('.//a/@title').extract_first()
            href = item.xpath('.//a/@href').extract_first()
            img = item.xpath('.//a//img/@src').extract_first()
            who = item.css('.who::text').extract_first()
            publisher = item.css('.who').css('.mb10::text').extract_first()
            price = item.css('.price::text').extract_first()
            old_price = item.css('.old-price::text').extract_first()
            discount = item.css('.discount-category::text').extract_first()
            yield {
                'title'     : title,
                'url'       : href,
                'img'       : img,
                'who'       : who,
                'publisher' : publisher,
                'price'     : price,
                'old_price' : old_price,
                'discount'  : discount,
            }
