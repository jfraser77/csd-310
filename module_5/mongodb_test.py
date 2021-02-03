"""
    Title: pytech collection
    Author: Joe Fraser
    Date: 1/31/21
    Description: Test program for showing student collection
"""




import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kxhod.mongodb.net/pytech.students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())
print("End of program, press any key to exit...")