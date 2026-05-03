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
    for fighter in results:
        print(f"{fighter[1]}{fighter[2]}{fighter[3]}{fighter[4]}{fighter[5]}")

    #loop finished here
    db.close()

#main code
print_all_aircraft()