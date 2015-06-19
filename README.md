Craigslist-Pricing-Project
==========================

1. Enter directory that you want to store the scraper and then in CMD enter: 

      scrapy startproject tutorial

2. Change base url to specific craigslist apartment link e.g. http://sfbay.craigslist.org/search/apa for San Francisco

3. To run the scraper type in the directory: 

    scrapy crawl craig -o items.csv -t csv

For more in-depth to customize, here's the blog post:

https://racketracer.wordpress.com/2015/01/29/practical-scraping-using-scrapy/

Replace the pipelines.py file with an empty file if you don't want to store the data in a postgresql database. 

