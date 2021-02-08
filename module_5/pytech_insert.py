"""
    Title: pytech insert
    Author: Joe Fraser
    Date: 2/1/21
    Description: Inserting documents practice
"""

""" Import statements """
from pymongo import MongoClient


# MongDB connection
url = "mongodb+srv://admin:admin@cluster0.kxhod.mongodb.net/pytech.students?retryWrites=true&w=majority"


# Connect pytech database
client = MongoClient(url)

# Connect to the MongoDB cluster
db = client.pytech


timothy = {
    "Student_Id": "1007",
    "First_Name": "Timothy",
    "Last_Name": "Biscuit",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.2",
            "start_date": "August 05, 2020",
            "end_date": "December 15, 2020",
            "courses": [
                {
                    "course_id": "SE710",
                    "description": "Socio Economics",
                    "instructor": "Kim Bass",
                    "grade": "B-"
                },
                {
                    "course_id": "HE311",
                    "description": "Philosphy",
                    "instructor": "Kyle Penn",
                    "grade": "A"
                }
            ]
        } 
    ]
}   

        



trunks = {
    "Student_Id": "1008",
    "First_Name": "Trunks",
    "Last_Name": "Bulma",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.65",
            "start_date": "January, 2020",
            "end_date": "May 12, 2020",
            "courses": [
                {
                    "course_id": "OS888",
                    "description": "European History",
                    "instructor": "Professor Theodore",
                    "grade": "B-"
                },
                {
                    "course_id": "EC200",
                    "description": "Election Politics",
                    "instructor": "Solomon Ezekial",
                    "grade": "C-"
                }
            ]
        } 
    ]
} 





yamcha = {
    "Student_Id": "1009",
    "First_Name": "Yamcha",
    "Last_Name": "Goku",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "3.0",
            "start_date": "June 12, 2020",
            "end_date": "August 02, 2020",
            "courses": [
                {
                    "course_id": "TS112",
                    "description": "Children Psychology",
                    "instructor": "Professor Huffman",
                    "grade": "A+"
                },
                {
                    "course_id": "CS517",
                    "description": "Computer Science",
                    "instructor": "Richard Smith",
                    "grade": "A"
                }
            ]
        } 
    ]
} 

# get the students colletion
print("\n  -- INSERT STATEMENTS --")

# insert statements with output
timothy_student_id = db.students.insert_one(timothy).inserted_id
print("Inserted student record Timothy Biscuit in the the students collection with document id", timothy_student_id)


trunks_student_id = db.students.insert_one(trunks).inserted_id
print("  Inserted student record Trunks Bulma in the the students collection with document id", trunks_student_id)

yamcha_student_id = db.students.insert_one(yamcha).inserted_id
print("  Inserted student record Yamcha Goku in the the students collection with document id", yamcha_student_id)


input("\n\nEnd of program, press any key to exit...")