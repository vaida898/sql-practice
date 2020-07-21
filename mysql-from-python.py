import os
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
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # Close the connection, regardless of wether the above was successful
    connection.close()
