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
        row = ("Bob", 21, "1990-02-06 23:04:06")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()

finally:
    # Close the connection, regardless of wether the above was successful
    connection.close()
