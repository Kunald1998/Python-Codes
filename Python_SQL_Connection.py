# Below import is not come with the default python installation, we need to import that using pip utility.
import mysql.connector

def main():
    # mysql.connector.connect() this method throws the object. To catch that object we created one variable as "mydatabaes".
    # Below method is use to create connection between the live data base and Python program.
    
    mydatabase = mysql.connector.connect(host="localhost",user="root") # In xampp the SQL that i have username is root and this user not have any password.
    # Above method required three parameters and that is host, user, password.
    # Below syntax is an object that is used to make the connection for executing SQL queries.
    query = mydatabase.cursor() # create cursor class object.

    # Below execute() method is use to run/fire the SQL query. 
    # Below query.execute("use MarvellousInfosystems") is important to select the database for fire the query on that data base.
    query.execute("use MarvellousInfosystems") # To execute query use cursor class object with execute() method.
    
    # Now we can run the query.
    query.execute("select * from student")
    #query.execute("select Name from student where RollNo= 15")
    #query.execute("show tables")
    
    for i in query:
        print(i)
    
    query.close() # This method s used to close the cursor object.

if __name__ == "__main__":
    main()

# mysql.exe -u root -p 
# here u = user & p = password
# user = root 
# password = enter provided password at the time of installing the MYSQL.