# Name: Abhishek Upadhyaya
# Module 6 - Assignment 6.3

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

# Get all the students in the collection in docs variable
docs = students.find()

# Iterate through all the documents and print on console
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

# Insert a new student with id 1010
new_student = {
    "student_id": "1010",
    "first_name": "Student",
    "last_name": "Four"
}
print("-- INSERT STATEMENTS --")
print(f"Inserted student record into the students collection with document id {students.insert_one(new_student).inserted_id}\n")

# Find document with student_id 1010 and print the same
print("-- DISPLAYING STUDENT TEST DOC --")
s1010 = students.find_one({"student_id": "1010"})
print(f"Student ID: {s1010['student_id']}")
print(f"First Name: {s1010['first_name']}")
print(f"Last Name: {s1010['last_name']}")

# Delete test student doc with id 1010
students.delete_one({"student_id": "1010"})

# Get all the students in the collection in docs variable
docs = students.find()

# Print empty line
print()

# Iterate through all the documents and print on console
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")