import pymongo
import json

connectionToMongo = pymongo.MongoClient("mongodb+srv://ProjectCoucou:THEpassword>@cluster0.ekjezah.mongodb.net/?retryWrites=true&w=majority")
db = connectionToMongo["Coucou"]
dbcollection = db["CoucouFiles"]
