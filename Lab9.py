from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import random
import datetime

client = MongoClient('localhost',27017)
db = client.csci2963
collection = db.definitions

#Print all documents
cursor = collection.find({})
for document in cursor:
    print(document)

print()

#Find one word by tag as well as by id
print(collection.find_one({"word":"Za"}))
print(collection.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b949')}))

print()

#Insert new document via python
collection.insert_one({"word":"Cadet Dascem","Zoomie scrub"})
print(collection.find_one({"word":"Cadet Dascem"}))

#Randomly print one document, update its time
ct = collection.count()
print()
randoc = collection.find()[random.randrange(ct)]
print("randoc is ", randoc["word"])
date =  datetime.date.today()
datestr = date.strftime('%m/%d/%Y')
collection.update_one({"word":randoc["word"]}, {"$push" : {"dates": datestr}})
randoc1 = collection.find_one({"word":randoc["word"]})
print(randoc1)
