# #This function creates the tables if they don't exist, mostly I'll keep this here as reference to create 
# #new tables in future projects
# import sqlite3
# DB_NAME = 'users.db'


# def init_db():
#     #Connects to the db; creates table if doesn't exist
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor() #creates cursor to execute sql commands

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS login (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             user_id INTEGER,
#             event TEXT,
#             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#             FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
#         );
#     """)

#     # Create the users table
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             phone TEXT UNIQUE NOT NULL,
#             isOnline INT,
#             isAdmin INT
           
#         );
#     """)
#     conn.commit()
#     conn.close()

# init_db()


#This block adds a new collumn to an existing table

# def add_column():
#     # Connect to the database
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     # Add new column to the table
#     cursor.execute("""
#         DROP TABLE users;
        
#     """)

#     conn.commit()
#     conn.close()


# add_column()
