import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": "Highway 37" }
newvalues = { "$set": { "address": "Park Lane 38" } }
mycol.update_many(myquery, newvalues)
print("Documents updated:", mycol.modified_count)
