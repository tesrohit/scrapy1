import scrapy
from pymongo import MongoClient

class home_spider(scrapy.Spider):
	name = "home"
	allowed_domains = ["zillow.com"]
	start_urls = [
		"http://www.zillow.com/homes/for_sale/Austin-TX/10221_rid/30.630231,-97.240677,29.98646,-98.265152_rect/9_zm/"
	]

	def parse(self,response):
		try:
			client = MongoClient()
			print "Connected"
		except Exception, e:
			print "not connected"
		db = client.sitedb
		collection = db.siteslist
		sites = response.xpath('//dt[@class="property-address"]/span/span/a/@href').extract()
		i = 0

		for x in sites:
			x = x.encode('utf-8')		
			x = "www.zillow.com" + x
			#print str(i)  + " " + x
			collection.insert({"sites":i,"link":x})			
			i = i + 1
		title = response.xpath('//header[@class="zsg-content-header addr"]/h1/text()').extract()
		pass
		
