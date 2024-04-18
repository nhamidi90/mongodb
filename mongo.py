import os
import pymongo
import pymongo.errors
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo DB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# insert one entry
# new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "hair_color": "grey", "ocupation": "writer", "nationality": "british"}

# insert more than one entry
# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]

# commit one entry
# coll.insert_one(new_doc)

# commit more than one entry
# coll.insert_many(new_docs)

# remove specific entry
# coll.delete_one({"first": "douglas"})

# update specific entry
# coll.update_one({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

# update more than one entry
coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

# find specific entry
# documents = coll.find({"first": "douglas"})

# find all instances
documents = coll.find()

for doc in documents:
    print(doc)