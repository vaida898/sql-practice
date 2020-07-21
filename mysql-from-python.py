import os
import datetime
import pymysql

# get username from Cloud9 workspace
# modify this variable if running on another environment
username = os.getenv('C9_USER')

# connect to a database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run the query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the 
        # table already exists


finally:
    # Close the connection, regardless of wether the above was successful
    connection.close()
