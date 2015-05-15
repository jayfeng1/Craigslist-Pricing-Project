# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 18:55:53 2015

@author: Jay
"""

#models.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()
# <--snip-->
class Apts(DeclarativeBase):
    __tablename__ = "seattle"
    
    craigId = Column('craigId', BigInteger, primary_key=True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
    price = Column('price', Integer, nullable=False)
    #area = Column('area', String, nullable=True)
    beds = Column('beds', Integer, nullable=False)
    size = Column('size', Integer, nullable=False)
    date = Column('date', String, nullable=False)
    numPic = Column('numPic', Integer, nullable=True)
    postDate = Column('postDate', DateTime, nullable=False)
    updateDate = Column('updateDate', DateTime, nullable=False)
    reposts = Column('reposts', Integer, nullable=False)
    contentLen = Column('contentLen', Integer, nullable=False)
    baths = Column('baths', Float, nullable=False)
    latitude = Column('latitude', Float(Precision=8), nullable=False)
    longitude = Column('longitude', Float(Precision=8), nullable=False)
    zipcode = Column('zipcode', String, nullable=False)

def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)

def db_connect():
    return create_engine(URL(**settings.DATABASE))