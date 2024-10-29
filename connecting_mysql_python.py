# The text below is used to install the MySQL Python Connector 'pip install mysql-connector-python'
# To use the connector in a file of code use the import statement
import mysql.connector
from mysql.connector import Error

# Function to open a database connection
def connect_database():
    # Database Connection Parameters:
    db_name =   # “your_dbname”
    user =      # “your_username”
    password =  # “your_password”
    host =      # “your_host”


    try: # Establishing the database connection
        conn = mysql.connector.connect(
	        database=db_name,
	        user=user,
	        password=password,
	        host=host
        )

        # Verifying the connection 
        print("Connected to MySQL database successfully.")
        return conn

    except Error as e: # Error handling
        print(f"Error: {e}")

    # finally: # Closing the connection
    #     if conn and conn.is_connected():
    #         conn.close()
    #         print("MySQL connection is closed.")