# Import the connect_database function
from connecting_mysql_python import connect_database

# Establishing database connection
conn = connect_database()

# Checking for successful database connection
if conn is not None:
    try:
        cursor = conn.cursor() # Activating the cursor

        # Query to remove an order for a customer
        query = """
        SELECT o.id AS OrderID, o.date AS OrderDate, c.id AS CustomerID, c.name, c.email
        FROM Customers c, Orders o
        WHERE c.id = o.customer_id AND c.name LIKE "John";
        """
        cursor.execute(query) # Executing the query

        # Fetching data and displaying the results
        for order in cursor.fetchall():
            print(order)

    except Exception as e: # Exception handling
        print(f"Error: {e}")

    # Closing cursor and connection
    finally:
        cursor.close()
        conn.close()