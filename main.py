#!/usr/bin/python3
#imports necessary modules
import csv, os, sys, writeBash as b, writeSQL as sql, delUsers as d


#creates bash files for creating users
try:
    f = open("create_users.sh", "w+")
except OSError as e:
        print("error " + e)
        sys.exit()
        
#inputs standard bash first line
f.write("#!/bin/bash\n\n")
#outputs program status
print("created shell file")

#creates sql file for creating users
try:
    sq = open("create_sql_users.sql", "w")
except OSError as e:
        print("error " + e)
        sys.exit()

#outputs program status
print("created sql file")

#creates shell file to delete users from list
try:
    bdel = open("delete_users.sh", "w")
except OSError as e:
    print("error " + e)
    sys.exit()

#output program status
print("created user delete shell file")



#opens file containing list of users
try:
    with open("/home/user/userlist.csv", 'r') as s:
        #creates a csv reader instance to read from file
        reader = csv.reader(s)
        #creates a loop to go through every single line in userlist file
        for row in reader:
            #makes a bash file to create users from the userlist file
            b.writeBash(f,'row[1].lower()+"."+row[0].lower()', row[2], row[1], row[0], row[3])
            #makes an sql fle to create sql users from the userlist file
            sql.writeSQL(sq, row[1], row[0], row[2], row[3])
            #Creates a file to delete all the users created with previous bash file
            d.writeBash(bdel, row[1].lower()+"."+row[0].lower())

    #closes the bash and sql files
    f.close()
    sq.close()
    bdel.close()
    
    #outputs finish message
    print("Mission Complete")
except OSError as e:
    print("Error " + e)
    sys.exit()
