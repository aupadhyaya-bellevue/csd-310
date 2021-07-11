# Name: Abhishek Upadhyaya
# Module 9 - Assignment 9.3

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


def printAllPlayersWithTeamName(cursor):
    # Define inner join query
    query = "SELECT player_id, first_name, last_name, team_name FROM player " \
            "INNER JOIN team ON team.team_id = player.team_id " \
            "ORDER BY player_id"

    # Execute above query and print all the result set
    cursor.execute(query)
    players = cursor.fetchall()
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team Name: {player[3]}\n")


try:
    # Connect to MySQL database with the configurations created above
    db = mysql.connector.connect(**config)

    # This statement will be printed if connection is successful
    print("\nDatabase user {} connected to MySQL on host {} with database {}"
          .format(config["user"], config["host"], config["database"]))

    # Open cursor
    cursor = db.cursor()

    # Build query to insert new player
    query = "INSERT INTO player(first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1);"
    cursor.execute(query)

    # Call function to print all the player records
    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    printAllPlayersWithTeamName(cursor)

    # Build query to update Smeagol's team to 'Team Sauron'
    query = "UPDATE player SET team_id = 2 WHERE first_name = 'Smeagol';"
    cursor.execute(query)

    # Call function to print all the player records
    print("\n-- DISPLAYING PLAYERS AFTER UPDATE --")
    printAllPlayersWithTeamName(cursor)

    # Build query to delete Smeagol's record
    query = "DELETE FROM player WHERE first_name = 'Smeagol';"
    cursor.execute(query)

    # Call function to print all the player records
    print("\n-- DISPLAYING PLAYERS AFTER DELETE --")
    printAllPlayersWithTeamName(cursor)

    # Close cursor
    cursor.close()
    # Close database
    db.close()

    # Ask user to acknowledge before program exits
    input("\n Press any key to continue...")

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
