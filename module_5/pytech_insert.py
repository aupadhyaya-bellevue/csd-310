# Name: Abhishek Upadhyaya
# Module 5 - Assignment 5.3

# Import pymongo module
import pymongo
from pymongo import MongoClient

# Assign mongodb connection string to variable named url
url = "mongodb+srv://admin:admin@cluster0.murgk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Create MongoClient object
client = MongoClient(url)

# Connect to database and assign the same to variable named db
db = client.pytech

# Assign students collection to students variable
students = db["students"]

# Declare student dictionaries
student1 = {
    "student_id": "1007",
    "first_name": "Student",
    "last_name": "One"
}
student2 = {
    "student_id": "1008",
    "first_name": "Student",
    "last_name": "Two"
}
student3 = {
    "student_id": "1009",
    "first_name": "Student",
    "last_name": "Three"
}

# Insert above students to collection and capture student ids
# student1_id = students.insert_one(student1).inserted_id
# student2_id = students.insert_one(student2).inserted_id
# student3_id = students.insert_one(student3).inserted_id

print("-- INSERT STATEMENTS --")
# Insert all the students and print document ids
print(f"Inserted student record Student One into the students collection with document id {students.insert_one(student1).inserted_id}")
print(f"Inserted student record Student One into the students collection with document id {students.insert_one(student2).inserted_id}")
print(f"Inserted student record Student One into the students collection with document id {students.insert_one(student3).inserted_id}")
