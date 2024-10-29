# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        cursor = conn.cursor() # Activating the cursor
        
        # Identifying details to use in query
        customer_id = 5
        order_id = 1

        # Query to remove an order for a customer
        query = "DELETE FROM Orders WHERE id = %s AND customer_id = %s"
        cursor.execute(query, (order_id, customer_id)) # Executing the query
        conn.commit() # Committing the query
        print("Order removed successfully.")

    # Closing cursor and connection
    finally:
        cursor.close()
        conn.close()