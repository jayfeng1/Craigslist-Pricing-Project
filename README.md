Craigslist-Pricing-Project
==========================

1. Enter directory that you want to store the scraper and then in CMD enter: 

      scrapy startproject tutorial

2. Change base url to specific craigslist apartment link e.g. http://sfbay.craigslist.org/search/apa for San Francisco

3. To run the scraper type in the directory: 

    scrapy crawl craig -o items.csv -t csv



