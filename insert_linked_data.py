# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        cursor = conn.cursor() # Activating the cursor
        
        # Identifying details to use in query
        john_doe_id = 5
        order_date = "2024-01-15"

        # Query to add an order for John Doe
        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"
        cursor.execute(query, (order_date, john_doe_id)) # Executing the query
        conn.commit() # Committing the query
        print("Order added successfully for John Doe.")

    # Closing cursor and connection
    finally:
        cursor.close()
        conn.close()