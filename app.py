from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ProjectCoucou:THEproject@cluster0.ekjezah.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Coucou"]
dbcollection = db["CoucouFiles"]

# Send a ping to confirm a successful connection
try:
    data = {
        "Message": "Hello!"
    }

    dbcollection.insert_one(data)
except Exception as e:
    print(e)