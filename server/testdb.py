import pymongo
url = "mongodb+srv://Cherlord1:Cherlord1@cluster0.2img3.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client["Database"]

a = db['Accounts']
print(db.list_collection_names())