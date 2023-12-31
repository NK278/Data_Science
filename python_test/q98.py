import pymongo
try:
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["mydatabase"]
  mycol = mydb["customers"]
except pymongo.errors.ConnectionFailure as err:
  print("Could not connect to MongoDB: {}".format(err))
else:
  mydict = { "name": "John", "address": "Highway 37" }
  x = mycol.insert_one(mydict)
  print(x.inserted_id)
finally:
  myclient.close()