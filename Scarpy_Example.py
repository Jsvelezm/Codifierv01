# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:36:31 2019

@author: FAMILIA
"""

### este es un ejemplo para demostrar mis habilidades con scrapy


import scrapy



class HomeCenterSpider(scrapy.Spider):
    name = 'HomeCenter_Spider'
    start_urls = ['https://www.homecenter.com.co/homecenter-co/category/cat300026/Pulidoras?sTerm=pulidora&sScenario=BRD_pulidora']
            
    
    def parse(self, response):
        articulo = "//section[@class='col-md-3 col-xs-12 col-sm-12 item jq-item one-prod']"
        for arti in response.xpath(articulo):

            articu = ".//p[@class='brand jq-brand']/a/text()"
            sku = ".//p[@class='sku']/text()"
            pr = ".//span[@itemprop='price']/text()"
            ahorro= ".//p[@class='normal-price PLP-EVENT_DIF_PRICE-2']/text()"
            yield {
                'name': arti.xpath(articu).extract_first(),
                'sku': arti.xpath(sku).extract_first()
                ,'price': arti.xpath(pr).extract_first()
                ,"ahorro": arti.xpath(ahorro).extract_first()}
            
            
        NEXT_PAGE_SELECTOR = '.next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )    