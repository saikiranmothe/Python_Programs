import pymongo

from pymongo import MongoClient


# connect to database
db = MongoClient('localhost', 27017)

collec = db.exp_development

# handle to names collection
names = collec.users.find()

print(names)

