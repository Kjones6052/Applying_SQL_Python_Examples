# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        # Activating the cursor
        cursor = conn.cursor() 

        # Creating a new customer
        new_customer = ("John Doe", "john.doe@example.com", "1234567890")  

        # Query to add the new customer
        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)" 

        # Executing the query
        cursor.execute(query, new_customer) 

        # Committing the changes to the database
        conn.commit()

        # Using a print statement to verify 
        print("New customer added successfully.")

    # Closing the connection and cursor
    finally: 
        cursor.close()
        conn.close()

