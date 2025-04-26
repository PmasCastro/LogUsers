#takes care of user authentication, login, logouts

import sqlite3

DB_NAME="users.db"

class Authenticator:

    def __init__(self):
        pass
    
    def login(self, username):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT isOnline FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        
        if result is None:
            print(f"User '{username}' does not exist.")
            conn.close()
            return
        if result[0] == 1:
            print(f"User '{username}' is already logged in")
            conn.close()
            return
        else:
            cursor.execute("SELECT id FROM users WHERE username=?", (username,))
            user = cursor.fetchone()
            user_id = user[0]
            cursor.execute(
                "UPDATE users SET isOnline=1 WHERE username =?", (username,)
                )
            cursor.execute(
                "INSERT INTO login (username, user_id, event) VALUES (?, ?, ?)",
                (username, user_id, "login")
            )
            conn.commit()
            print(f"User '{username}' is logged in")
            conn.close()
    

    def logout(self, username):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET isOnline=0 WHERE username =?", (username,)
            )
        
        cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        user_id = user[0]
        cursor.execute("INSERT INTO login(username, user_id, event) VALUES (?, ?, ?)",
                       (username, user_id, "logout")
                       )

        conn.commit()
        print(f"User '{username}' is logged out")
        conn.close()

    
user_login = Authenticator()

user_login.logout("Admin")




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
#             isOnline INT,
#             isAdmin INT
           
#         );
#     """)
#     conn.commit()
#     conn.close()

# init_db()



