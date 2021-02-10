"""
    Title: pytech delete
    Author: Joe Fraser
    Date: 2/1/21
    Description: insert new files and deletion practice
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

# added new document
zander = {"Student_Id": "1010", "First_Name": "Zander", "Last_Name": "Cage"}

# inset document into database
zander_doc = db.students.insert_one(zander).inserted_id

# output statements from insert
print("\n -- INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id " + str(zander_doc))

# Call the find_one() method and display the results to the terminal window.
student_zander_doc = db.students.find_one({"Student_Id": "1010"})

# Results into Terminal
print("\n DISPLAYING STUDENT TEST DOC --")
print(" Student ID: " + student_zander_doc["Student_Id"] + "\n First Name: " + student_zander_doc["First_Name"] +"\n Last Name: " + student_zander_doc["Last_Name"] + "\n")

# Call the delete_one() method by student_id 1010.
delete_zander_doc = db.students.delete_one({"Student_Id": "1010"})

# Call the find() method and display the results to the terminal window.
new_studentlist = db.students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over output the results
for doc in student_listing:
    print(" Student ID: " + doc["Student_Id"] + "\n First Name: " + doc["First_Name"] + "\n Last Name: " + doc["Last_Name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")