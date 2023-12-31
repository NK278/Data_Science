import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
pipeline = [
  { "$match": { "address": "Highway 37" } },
  { "$group": { "_id": "$name", "count": { "$sum": 1 } } }
]
result = mycol.aggregate(pipeline)
for x in result:
  print(x)