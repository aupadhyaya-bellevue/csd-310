# Import pymongo module
import pymongo
from pymongo import MongoClient

# Assign mongodb connection string to variable named url
url = "mongodb+srv://admin:admin@cluster0.murgk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Create MongoClient object
client = MongoClient(url)

# Connect to database and assign the same to variable named db
db = client.pytech

# Print list of all collections
print(db.list_collection_names())

