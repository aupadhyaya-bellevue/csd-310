# Name: Abhishek Upadhyaya
# Module 8 - Assignment 8.2

# Import MySQL modules
import mysql.connector
from mysql.connector import errorcode

# Define database configurations
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    # Connect to MySQL database with the configurations created above
    db = mysql.connector.connect(**config)

    # This statement will be printed if connection is successful
    print("\n Database user {} connected to MySQL on host {} with database {}"
          .format(config["user"], config["host"], config["database"]))

    # Close database
    db.close()

    # Ask user to acknowledge before program exits
    input("\n\n Press any key to continue...")

# Catch possible errors while connecting to database
except mysql.connector.Error as err:

    # Check if database connection failed because of bad credentials
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    # Check if connection failed because invalid database name is provided in config
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database doesn't exist")
    # Some other error occurred
    else:
        print(err)
