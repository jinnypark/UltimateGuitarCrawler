import scrapy
import time
from selenium import webdriver

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from ug_crawler.items import UgCrawlerItem

class UGSpider(scrapy.Spider):
    print("class has been created.")
    name = "UltimateGuitar"
    rotate_user_agent = True
    allowed_domains = ["ultimate-guitar.com"]
        
    content = []
    with open('/Users/jinnykittiy/Box Sync/DataMining/UGproject_practice/scrapy/ug_links/links_topRated1980s_20pgs.txt') as f:
        content = content + f.readlines()
        # Remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
    #start_urls = ["https://tabs.ultimate-guitar.com/tab/kodaline/all_i_want_chords_1180259"]
    print("this would have been start urls: ", content)
    start_urls = content
    #start_urls = ["https://tabs.ultimate-guitar.com/tab/jeff_buckley/hallelujah_chords_198052","https://tabs.ultimate-guitar.com/tab/jason_mraz/im_yours_chords_373896","https://tabs.ultimate-guitar.com/tab/oasis/wonderwall_chords_39144","https://tabs.ultimate-guitar.com/tab/pink_floyd/wish_you_were_here_chords_44555","https://tabs.ultimate-guitar.com/tab/train/hey_soul_sister_chords_884388"]
    
    def __init__(self):
        print("initializing")
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("/Users/jinnykittiy/chromedriver")
        print("finished initializing")
    def parse(self, response):
        print("starting to get browser")
        self.browser.get(response.url)
        print("time to sleep")
        time.sleep(5)
        print("done sleeping")
        
        print("time to find element by xpath")
        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        if html == "":
            print("Failed to scrape html content")
        else:
            print("html successfully acquired!", "\n")
        print("let's use selector")
        
        selector = Selector(text=html)
        item = UgCrawlerItem()
        metaList = selector.xpath('//meta').extract()
        print("here is metadata scraped: ", "\n", metaList)
        
        item["meta_title"] = metaList[2]
        item["URL"] = response.request.url
        item["meta_description"] = metaList[3]#important for checking duplicates
        #item["meta_image"] = metaList[4]
        #    item["meta_contentDescription"] = row.xpath('./meta[5]/text()')[0].extract()
        item["meta_keywords"] = metaList[6]
        #    item["meta_viewport"] = row.xpath('./meta[8]/text()')[0].extract()
        #    item["meta_application_name"] = row.xpath('./meta[12]/text()')[0].extract()
        #    item["meta_csrf_token"] = row.xpath('./meta[11]/text()')[0].extract()
        
       # item["chords"] = selector.xpath('/html/body/div[1]/section/div/div/main/div[2]/div[2]/section/article/div[1]/div/section[2]/section/pre/span[text()]/text()').extract()
        
        item["chords"] = selector.xpath('/html/body/div[1]/div/div[2]/main/div[2]/div[3]/article/div[1]/div/section[2]/section/pre/span[text()]/text()').extract()
                                       # /html/body/div[1]/div/div[2]/main/div[2]/div[1]/article/div[1]/div/section[2]/section/pre/span[14]
                                       # /html/body/div[1]/div/div[2]/main/div[2]/div[1]/article/div[1]/div/section[2]/section/pre/span[33]
                                       # /html/body/div[1]/div/div[2]/main/div[2]/div[1]/article/div[1]/div/section[2]/section/pre/span[6]
        print("here is a list of chords: ", selector.xpath('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/article/div[1]/div/section[2]/section/pre/span[text()]/text()').extract(), "/n")  
        yield item
        
