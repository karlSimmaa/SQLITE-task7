#docstring- Karl R.- airplane database application\\\\\\
#imports
import sqlite3


#contants and variables
DATABASE = "fighters.db"

#functions
def print_all_aircraft():
    """print all the aircraft nicely"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name    speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()

#main code
while True:
    #get the user's input
    user_input = input("\nWhat would you like to do.\n1. Print all aircraft\n7. Exit\n")

#conditions
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")