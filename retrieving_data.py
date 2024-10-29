# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing the database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        # Activating the cursor
        cursor = conn.cursor() 

        # Identifying the query to run
        query = "SELECT * FROM Customers" 

        # Executing the query
        cursor.execute(query) 

        # Fetching the data
        for row in cursor.fetchall(): 
            print(row) # Printing the data
    
    # Closing the connection and cursor
    finally: 
        cursor.close()
        conn.close()