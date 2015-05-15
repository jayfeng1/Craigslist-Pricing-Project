# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 13:51:04 2014

@author: Jay
"""

import pandas as pd

#TODO Check for duplicates
# Check for ID duplicates

zips = "C:/Users/Jay/Dropbox/Coding Projects/craigslist/ZipCodeSeattle.csv"
zipSeattle = pd.read_csv(zips)
data = "C:/Users/Jay/Dropbox/Coding Projects/craigslist/craigSeattle.csv"
craig = pd.read_csv(data)
craig['zipcode'] = NaN

for i in range(0, len(craig.coord)-1):
    valMin = 10
    for j in range(0, len(zipSeattle.latitude)-1):
        temp = findDist(craig.latitude[i], craig.longitude[i], zipSeattle.latitude[j], zipSeattle.longitude[j])
        if temp < valMin:
            valMin = temp
            craig.zipcode[i] = zipSeattle.zipcode[j]

craig = craig[craig.price < 15000]
craig = craig[craig.price > 100] 
craig = craig[craig.size < 10000]
craig.baths = double(craig.baths)
craig = craig[craig.baths < 10]

#craig = craig[craig.beds > 0]
#craig = craig[craig.size > 0]
craig = craig[craig.zipcode > 0]         
#df.loc[0] = pd.Series(item)
#Extra Clean

craig.to_csv("C:/Users/Jay/Dropbox/Coding Projects/craigslist/craig11_15Formatted.csv")
    
def findZip(address):
    for s in address:
        if len(s) == 5:
            print(s)
            return s
            
def findDist(lat, lon, dataLat, dataLon):
    return abs(lat-dataLat) + abs(lon - dataLon)
    
#Splicing
#sep = "["
#for i in range(0, len(neigh['NeighSubArea'])):
#    if sep in neigh['NeighSubArea'][i]:
#        neigh['NeighSubArea'][i] = neigh['NeighSubArea'][i].split(sep, 1)[0]

#if key returns value
#use value as new key
#recursive
#Seattle neighborhood 5-count

#Code for GeoPy Google API
#for i in range(0, len(craig.coord)-1):
#    location = geolocator.reverse(craig.coord[i]).address
#    if location is not None: 
#        zipcode = findZip(location.split(", "))
#        craig.zipcode[i] = zipcode
#        time.sleep(1)
#    print(i)



