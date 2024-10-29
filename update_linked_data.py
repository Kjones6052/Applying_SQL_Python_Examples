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
        new_order_date = "2024-02-20"

        # Query to update an order for a customer
        query = "UPDATE Orders SET date = %s WHERE id = %s AND customer_id = %s"
        cursor.execute(query, (new_order_date, order_id, customer_id)) # Executing the query
        conn.commit() # Committing the query
        print("Order updated successfully.")

    # Closing cursor and connection
    finally:
        cursor.close()
        conn.close()