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

# Assign all the docs in students collection to docs variable
docs = students.find()

# Iterate through all the documents and print on console
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

# Find document with student_id 1007 and print the same
print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY --")
s1007 = students.find_one({"student_id": "1007"})
print(f"Student ID: {s1007['student_id']}")
print(f"First Name: {s1007['first_name']}")
print(f"Last Name: {s1007['last_name']}")
