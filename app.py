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

def print_all_aircraft_by_speed(args):
    """print all the aircraft by speed"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name    speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()

def print_all_aircraft_by_g():
    """print all the aircraft by max g"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY max_g DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name    speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()

def print_all_aircraft_by_climb():
    """print all the aircraft by climb rate"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY climbrate DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name    speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()

def print_all_aircraft_by_range():
    """print all the aircraft by range"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name    speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()

def print_all_aircraft_by_payload():
    """print all the aircraft by payload"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY payload DESC;"
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
    user_input = input("1. Print all aircraft\n2. Print all aircraft by speed\n3. Print all aircraft by max g\n4. Print all aircraft by climb rate\n5. Print all aircraft by range\n6. Print all aircraft by payload\n7. Exit\n")

#conditions
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_g()
    elif user_input == "4":
        print_all_aircraft_by_climb()
    elif user_input == "5":
        print_all_aircraft_by_range()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")