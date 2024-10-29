# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        # Utilizing the cursor
        cursor = conn.cursor() 

        # Updating an existing customer
        updated_customer = ("9876543210", 3)  

        # Query to update the customer info
        query = "UPDATE Customers SET phone = %s WHERE id = %s" 

        # Executing the query
        cursor.execute(query, updated_customer) 

        # Committing the changes to the database
        conn.commit()

        # Using a print statement to verify 
        print("Customer updated successfully.")

    # Closing the connection and cursor
    finally: 
        cursor.close()
        conn.close()