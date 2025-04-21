#This file only handles db interactions: connects the db on init; adds new users; checks if user exists etc

import sqlite3
import bcrypt

DB_NAME = "users.db"

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



class User:
    def __init__(self, username, password, is_admin=False):
        self.username=username
        self.password=password
        self.is_admin=is_admin
    
    #Add new user to db
    def create_user(self):
        #encrypt the password
        hashed = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            #VALUES placeholder (?, ?, ?, ?) prevents SQL injection
            cursor.execute(
                "INSERT INTO USERS (username, password, isOnline, isAdmin) VALUES (?, ?, ?, ?)", 
                (self.username, hashed, 0, int(self.is_admin))
                )
            conn.commit()
            print(f"User '{self.username}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"User '{self.username}' already exists, please choose a different user name.")
        finally:
            conn.close()    
        
# #Example to create user
# admin_user = User("Andy", "1234", is_admin=False)
# admin_user.create_user()

        
# if __name__ == "__main__":
#     init_db()
#     # Uncomment the next line if you need to create admin user
#     # add_user("admin", "admin123")

