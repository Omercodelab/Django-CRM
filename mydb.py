import mysql.connector 

dateBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123',

)
#prepare a cursor Object
cursorObject = dateBase.cursor()

# Create a dataBase
cursorObject.execute("CREATE DATABASE firstdatabase")

print("All Done!")

cursorObject.close()
dateBase.close()