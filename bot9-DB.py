import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()

sample_data_query = """
    INSERT INTO users (id, first_name, last_name, phone_number)
    VALUES (?, ?, ?, ?)
"""

sample_data = [(4587, 'Ehsan', 'Abd', '9876542345'),
               (4525, 'jack', 'Abd', '9876542345'),
               (7854, 'Sarah', 'Abd', '9876542345'),
               (8548, 'Maryam', 'Abd', '9876542345')]

# with sqlite3.connect('user.db') as connection:
#     cursor = connection.cursor()
#     cursor.executemany(sample_data_query, sample_data)

fetch_data_query = """
    SELECT id, first_name, last_name, phone_number FROM users
"""
rows = []

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.execute(fetch_data_query)
    rows = cursor.fetchall()

for row in rows:
    print(f'ID:{row[0]}, FN:{row[1]}, LN:{row[2]}, PN:{row[3]}')

































# import sqlite3

# # Database file path
# DATABASE_FILE = 'user.db'

# # Function to create the database and table
# def create_database():
#     connection = sqlite3.connect(DATABASE_FILE)
#     cursor = connection.cursor()

#     # Create table query
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         phone_number TEXT NOT NULL
#     );
#     """
    
#     cursor.execute(create_table_query)
#     connection.commit()
#     connection.close()

# # Function to insert sample data into the users table
# def insert_sample_data():
#     connection = sqlite3.connect(DATABASE_FILE)
#     cursor = connection.cursor()
    
#     # Insert data query
#     insert_data_query = """
#     INSERT INTO users (first_name, last_name, phone_number)
#     VALUES (?, ?, ?);
#     """
    
#     # Sample data
#     sample_data = [
#         ('John', 'Doe', '1234567890'),
#         ('Jane', 'Smith', '0987654321'),
#         ('Alice', 'Johnson', '5555555555'),
#         ('Bob', 'Brown', '4444444444'),
#         ('Charlie', 'Davis', '3333333333')
#     ]
    
#     cursor.executemany(insert_data_query, sample_data)
#     connection.commit()
#     connection.close()

# # Create the database and table
# create_database()

# # Insert sample data
# insert_sample_data()

# # Function to fetch and display the data from the users table
# def fetch_and_display_data():
#     connection = sqlite3.connect(DATABASE_FILE)
#     cursor = connection.cursor()
    
#     # Fetch data query
#     fetch_data_query = "SELECT first_name, last_name, phone_number FROM users;"
    
#     cursor.execute(fetch_data_query)
#     rows = cursor.fetchall()
    
#     # Display data
#     for row in rows:
#         print(f"First Name: {row[0]}, Last Name: {row[1]}, Phone Number: {row[2]}")
    
#     connection.close()

# # Fetch and display the inserted data
# fetch_and_display_data()


