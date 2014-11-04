# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:02:19 2014

@author: Jay
"""

import scrapy


#Item class with fields to scrape
class CraigslistItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    beds = scrapy.Field()
    size = scrapy.Field()
    CraigID = scrapy.Field()
    numPic = scrapy.Field()
    coord = scrapy.Field()
    postDate = scrapy.Field()
    updateDate = scrapy.Field()
    content = scrapy.Field()
    beds1 = scrapy.Field()
    size1 = scrapy.Field()
    baths = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()

class MySpider(scrapy.Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    base_url = "http://seattle.craigslist.org/search/see/apa?"
    start_urls = ["http://seattle.craigslist.org/search/see/apa?"]
    #Initially grab all of the urls that craigslist allows
    for i in range(1, 24):
        start_urls.append(base_url + "s=" + str(i) + "00&")

    def parse(self, response):
        #find all postings
        postings = response.xpath(".//p")
        #loop through the postings
        for posts in postings:
            item = CraigslistItem()
            #grab craiglist apartment listing ID
            item["CraigID"] = posts.xpath("@data-pid").extract()
            temp = posts.xpath("span[@class='txt']")
            info = temp.xpath("span[@class='pl']")
            #title of posting
            item["title"] = info.xpath("a/text()").extract()
            #date of posting
            item["date"] = info.xpath("time/text()").extract()
            #pre-processing for getting the price in the right format
            price = ''.join(temp.xpath("span")[2].xpath("span[@class='price']").xpath("text()").extract())
            item["price"] = price.replace("$","")
            bedSize = temp.xpath("span")[2].xpath("text()")[1].extract()
            temp1 = bedSize.split("-")
            if(len(temp1) > 2):
                item["beds"] = temp1[0].strip().replace("/ ","").replace("br","")
                item["size"] = temp1[1].strip()
            elif("br" in bedSize):
                item["beds"] = temp1[0].strip().replace("/ ","").replace("br","")
            else:
                item["size"] = temp1[0].strip().replace("/ ","")
            #item["beds"] = posts.xpath("span")[2].xpath("text()")[1].extract()
            item["area"] = temp.xpath("span")[2].xpath("span[@class='pnr']").xpath("small/text()").extract()
            item["link"] = info.xpath("a/@href").extract()
            follow = "http://seattle.craigslist.org" +''.join(item["link"])
            #Parse request to follow the posting link into the actual post
            request = scrapy.Request(follow , callback=self.parse_item_page)
            request.meta['item'] = item
            yield request
            #items.append(item)
        #return items
    
    #Parsing method to grab items from inside the posting    
    def parse_item_page(self, response):
        item = response.meta["item"]
        maplocation = response.xpath("//div[contains(@id,'map')]")
        latitude = maplocation.xpath('@data-latitude').extract()
        longitude = maplocation.xpath('@data-longitude').extract()
        item["latitude"] = latitude
        item["longitude"] = longitude
        item["coord"] = ''.join(latitude) + ", " + ''.join(longitude)
        postinginfo = response.xpath("//p[@class = 'postinginfo']").xpath("time/@datetime")
        item["postDate"] = postinginfo[0].extract()
        item["updateDate"] = postinginfo[len(postinginfo)-1].extract()
        item["numPic"] = len(response.xpath("//div[@id='thumbs']").xpath("a"))
        return item
        
            
