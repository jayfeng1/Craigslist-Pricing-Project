# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
DOCUMENTATION
    
'''
from sqlalchemy.orm import sessionmaker
from models import Apts, db_connect, create_deals_table
from sqlalchemy import update
import csv

class CraigslistPipeline(object):
    
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)
        zipDict = self.createZip()
        global zipDict
        
    def createZip(self):
        zips = "C:/Users/Jay/Dropbox/Coding Projects/craigslist/ZipCodeSeattleOnly.csv"
        with open(zips) as csvfile:
            reader = csv.DictReader(csvfile)
            zipDict = {}
            for row in reader:
                zipDict[row['zipcode']] = {'latitude':row['latitude']}
                zipDict[row['zipcode']].update({'longitude':row['longitude']})
        return zipDict
        
    def findZip(self, zipDict, item):
        valMin = 10
        zip1 = ''
        for code in zipDict:
            temp = self.findDist(float(zipDict[code]['latitude']), float(zipDict[code]['longitude']), 
                    item['latitude'], item['longitude'])
            if temp < valMin:
                valMin = temp
                zip1 = code
        return zip1
    
    def findDist(self, lat, lon, dataLat, dataLon):
        return abs(lat-dataLat) + abs(lon - dataLon)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        global zipDict
        session = self.Session()
        item['zipcode'] = self.findZip(zipDict, item)
        #TODO: change to below if after a week or two
        #if item['reposts'] == 1:
        old = session.query(Apts.reposts).filter(Apts.craigId==item['craigId'])
        if old.all():
            #TODO:
            #if session.query(Apts.updateDate).filter(Apt
            update(Apts).where(Apts.craigId==item['craigId']).values(reposts=old+1)          
        else:
            deal = Apts(**item)
            try:
                session.add(deal)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
    
            return item