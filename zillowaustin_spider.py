from pymongo import MongoClient
import scrapy

class spider1(scrapy.Spider):
	name = "zillowaustin"
	allowed_domains = ["zillow.com"]
	start_urls = [
		
	]	

	
	try:
		client = MongoClient()
		print "Connected"
	except Exception, e:
		print "not connected"
		
	db = client.sitedb
	collection = db.siteslist
	sites = collection.find()
	i = 0
	for site in  sites:
		start_urls.insert(i,"http://" + site['link'].encode('utf-8'))
		i = i + 1
	

	def parse(self,response):
		filename = response.url.split("/")[-2]
		title = response.xpath('//header[@class="zsg-content-header addr"]/h1/text()').extract()
		title_addr = response.xpath('//span[@class="zsg-h2 addr_city"]/text()').extract()
		title_cont = response.xpath('//header[@class="zsg-content-header addr"]/h3/span/text()').extract()
		title_desc = response.xpath('//div[@class="notranslate"]/text()').extract()
		title_facts = response.xpath('//div[@class="hdp-facts zsg-content-component z-moreless"]/div[1]/ul/li/text()').extract()
		title_features = response.xpath('//div[@class="hdp-facts zsg-content-component z-moreless"]/div[2]/ul/li/text()').extract()
		title_images = response.xpath('//div[@class="thumb-nav"]/ol/li').extract()
		cont = title_cont[0] + "," + title_cont[1] + "," + title_cont[2]
		try:
			client = MongoClient()
			print "Connected"
		except Exception, e:
			print "not connected"
		db = client.sitedb
		collection = db.sitedata1
		collection.insert({"name":str(title[0][:-5]),"address":str(title_addr[0]),"content":cont,"desc":str(title_desc[0]),"facts":str(title_facts[0]),"features":str(title_features[0])})	
		
