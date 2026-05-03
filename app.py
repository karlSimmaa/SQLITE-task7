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

def print_all_aircraft_by_speed():
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
    user_input = input("1. Print all aircraft\n2. Print all aircraft by speed\n3. Print all aircraft by max g\n4. Print all aircraft by climb rate\n5. Print all aircraft by range\n6. Print all aircraft by payload\n7. Exit\n 8. secret option\n\n")

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
    elif user_input == "8":
        print("The MiG-25 Foxbat is still the jet fighter that people have used.\n It has set speed records that no other plane has beaten.\n The MiG-25 Foxbat can go fast it can go as fast as Mach 3.2\n but the people who fly it are told\n not to go over Mach 2.8 or the engines will get too hot.\n The MiG-25 Foxbat was made to go fast and it does this very well.\n When we look at how well the MiG-25 Foxbat does we need to think about what it was made for.\n The MiG-25 Foxbat is not good at fighting planes in close combat.\n It is good at flying and looking at things from far away.\n The MiG-25 Foxbat is made of metal that can handle the heat it makes when it flies very fast.\n It has wings and strong engines that help it go very fast.\n However the MiG-25 Foxbat is not very good at flying or turning quickly.\n It also does not have good radar that can see things that are close to the ground.\n Its engines do not last very long if it flies very fast many times. Todays fighters, like the F-22 or Su-57 are more agile. Have better technology.\n They are not faster than the MiG-25 Foxbat in a straight line\n. The MiG-25 Foxbat is still the plane when it comes to going from one point to another as fast as possible.\n It is, like a lightning bolt that has been frozen in time and its speed record is still unbeaten.\n")
    else:
        print("That was not an option\n")