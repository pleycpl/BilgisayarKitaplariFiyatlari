import scrapy
# scrapy crawl dr.com.tr-moreinfo -o out-dr-more.json

class DrSpider(scrapy.Spider):
    name = 'dr.com.tr-moreinfo'
    allowed_domains = ['dr.com.tr']
    start_urls = [
        'http://www.dr.com.tr/kategori/Kitap/Egitim-Basvuru/Bilgisayar'
    ]

    def parse(self, response):
        items = response.css('.item-name')
        for item in items:
            url = item.css('::attr(href)').extract_first()
            url = url[:-1] # space
            #title = item.css('::attr(title)')
            #price = item.css('.price::text').extract_first()
            #old_price = item.css('.old-price::text').extract_first()
            yield scrapy.Request(response.urljoin(url), callback=self.parse_books)

    def parse_books(self, response):
        product_name = response.css('h1.product-name::text').extract_first()
        author, publisher = response.css('.author').xpath('.//span/text()').extract()
        # price = response.css('.price::text').extract_first() , it doesnt working
        # old_price = item.css('.old-price::text').extract_first(), it doesnt working
        pic = response.css('.img-responsive::attr(src)').extract_first()
        content = response.css('.summary').xpath('.//p').extract_first() # we must strip <br> <b> and <p> tags
        comments = []
        for comment in response.css('.comment'):
            comment_content = {
                'content' : comment.css('.comment-content').extract_first(),
                'detail' : comment.css('.comment-details').extract_first(),
            }
            comments.append(comment_content)

        yield {
            'product_name' : product_name,
            'author' : author,
            'publisher' : publisher,
            'content' : content,
            'comments' : comments
        }
