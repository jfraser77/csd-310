"""
    Title: pytech insert
    Author: Joe Fraser
    Date: 2/1/21
    Description: Inserting documents practice
"""

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kxhod.mongodb.net/pytech.students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("-- INSERT STATEMENTS --")

timothy = {
    "Student_Id": "1007",
    "First_Name": "Timothy",
    "Last_Name": "Biscuit"
}

timothy_student_id = db.students.insert_one(timothy).inserted_id

print("Inserted student record Timothy Biscuit in the the students collection with document id", timothy_student_id)

trunks = {
    "Student_Id": "1008",
    "First_Name": "Trunks",
    "Last_Name": "Bulma"
}

trunks_student_id = db.students.insert_one(trunks).inserted_id

print("Inserted student record Trunks Bulma in the the students collection with document id", trunks_student_id)

yamcha = {
    "Student_Id": "1009",
    "First_Name": "Yamcha",
    "Last_Name": "Goku"
}

yamcha_student_id = db.students.insert_one(yamcha).inserted_id

print("Inserted student record Yamcha Goku in the the students collection with document id", yamcha_student_id)
print()
print("End of program, press any key to exit...")