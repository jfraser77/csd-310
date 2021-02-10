"""
    Title: pytech insert
    Author: Joe Fraser
    Date: 2/1/21
    Description: update documents practice
"""

""" Import statements """
from pymongo import MongoClient


# MongDB connection
url = "mongodb+srv://admin:admin@cluster0.kxhod.mongodb.net/pytech.students?retryWrites=true&w=majority"


# Connect pytech database
client = MongoClient(url)

# Connect to the MongoDB cluster
db = client.pytech

# query student collection
student_listing = db.students.find({})

# get the students collection
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over output the results
for doc in student_listing:
    print(" Student ID: " + doc["Student_Id"] + "\n First Name: " + doc["First_Name"] + "\n Last Name: " + doc["Last_Name"] + "\n")

# update 1007
result = db.students.update_one({"Student_Id": "1007"},{"$set": {"Last_Name": "Felix"}})

# find updated student doc
timothy = db.students.find_one({"Student_Id": "1007"})

# display 
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

# OUTPUT DOCUMENT UPDATE
print(" Student ID: "  + timothy["Student_Id"] + "\n First Name: " + timothy["First_Name"] + "\n Last Name: " + timothy["Last_Name"] + "\n")

# exit message 
input("\n\nEnd of program, press any key to exit...")
