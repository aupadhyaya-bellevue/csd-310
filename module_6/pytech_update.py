# Name: Abhishek Upadhyaya
# Module 6 - Assignment 6.2

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

# Update last name for the student with id 1007
result = students.update_one({"student_id": "1007"}, {'$set': {"last_name": "New Last Name"}})

# Find document with student_id 1007 and print the same
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
s1007 = students.find_one({"student_id": "1007"})
print(f"Student ID: {s1007['student_id']}")
print(f"First Name: {s1007['first_name']}")
print(f"Last Name: {s1007['last_name']}")
