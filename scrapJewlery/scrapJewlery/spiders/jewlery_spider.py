import scrapy
import re
from ..items import ScrapjewleryItem

class Jewlery(scrapy.Spider):
    name = 'necklace'

    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
    ]

    def parse(self, response):
        items = ScrapjewleryItem()
        all_li_necklace = response.css('#JsonProductList li')
        for text in all_li_necklace:
            neclace_desc = text.css('p::text').extract()
            neclace_price = text.css('span:nth-child(1)::text').extract()
            neclace_image_url = text.css('img::attr(data-original)').extract()
            neclace_image_with_lady = text.css('img::attr(onmouseover)').extract_first()
            neclace_image_with_lady = re.sub(r"this.src=", "", neclace_image_with_lady)
            neclace_image_with_lady = [re.sub(r"'", "", neclace_image_with_lady)]
            items['neclace_desc'] = neclace_desc
            items['neclace_price'] = neclace_price
            items['neclace_image_url'] = neclace_image_url
            items['neclace_image_with_lady'] = neclace_image_with_lady
            yield items
