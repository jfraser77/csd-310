"""
    Title: pytech insert
    Author: Joe Fraser
    Date: 2/1/21
    Description: Query documents practice
"""

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kxhod.mongodb.net/pytech.students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Find() method to display all documents in the collection.
docs = db.students.find({
    "Student_Id": "1007",
    "First_Name": "Timothy",
    "Last_Name": "Biscuit"
}

{
    "Student_Id": "1008",
    "First_Name": "Trunks",
    "Last_Name": "Bulma"
}

{
    "Student_Id": "1009",
    "First_Name": "Yamcha",
    "Last_Name": "Goku"
})

for doc in docs:
    print(doc)

# findOne() method to display a single document by student id
doc = db.students.find_one({"student_id": "1007"})

print(doc["student_id"])
print()
print("End of program, press any key to continue...")