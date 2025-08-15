import mysql.connector

connection = None  # Initialize connection variable

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ALXafrica@25"   # Your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    # This exact exception form is required by the checker
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close the connection safely
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
