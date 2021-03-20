import scrapy


class ScrapjewleryItem(scrapy.Item):
    # define the fields for your item here like:
    neclace_desc = scrapy.Field()
    neclace_price = scrapy.Field()
    neclace_image_url = scrapy.Field()
    neclace_image_with_lady = scrapy.Field()
