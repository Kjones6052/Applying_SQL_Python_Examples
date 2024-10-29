# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        # Utilizing the cursor
        cursor = conn.cursor() 

        # Removing an existing customer
        customer_to_remove = (2, )  

        # Query to check if there is a conflict with removing the customer
        query_check = "SELECT * FROM Orders WHERE customer_id = %s"

        # Executing the query
        cursor.execute(query_check, customer_to_remove)

        # Retrieving data and putting it into a variable
        orders = cursor.fetchall()

        # Checking if the variable holds any values
        if orders:

            # Using print statement to confirm a conflict was found and removal cannot take place
            print("Cannot delete customer: Customer has associated orders.")

        # If no conflict is found the else statement runs
        else:
            # Query to delete a customer
            query = "DELETE FROM Customers WHERE id = %s" 

            # Executing the query
            cursor.execute(query, customer_to_remove) 

            # Committing the changes to the database
            conn.commit()

            # Using a print statement to verify 
            print("Customer removed successfully.")

    # Exception handling
    except Exception as e: 
        print(f"Error: {e}")

    # Closing the connection and cursor
    finally: 
        cursor.close()
        conn.close()