# def init_db():
#     #Connects to the db; creates table if doesn't exist
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor() #creates cursor to execute sql commands

#     # Create the users table
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL,
#             isOnline INT,
#             isAdmin INT
           
#         );
#     """)
#     conn.commit()
#     conn.close()