# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundrazorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    campaignTitle = scrapy.Field()
    #amountRaised = scrapy.Field()
    goal = scrapy.Field()
    currencyType = scrapy.Field()
    #endDate = scrapy.Field()
    numberContributors = scrapy.Field()
    story = scrapy.Field()
    url = scrapy.Field()
    pass
