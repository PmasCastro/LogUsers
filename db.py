#This file only handles db interactions: connects the db on init; adds new users; checks if user exists etc
import sqlite3
import bcrypt

DB_NAME = "users.db"

class User:
    def __init__(self, username, password, is_admin=False):
        self.username=username
        self.password=password
        self.is_admin=is_admin
    
    #Add new user to db
    def create_user(self):
        if " " in self.username:
            print("Username cannot contain spaces")
            return
        
        #encrypt the password
        hashed = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            #VALUES placeholder (?, ?, ?, ?) prevents SQL injection
            cursor.execute(
                "INSERT INTO users (username, password, isOnline, isAdmin) VALUES (?, ?, ?, ?)", 
                (self.username, hashed, 0, int(self.is_admin))
                )
            conn.commit()
            print(f"User '{self.username}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"User '{self.username}' already exists, please choose a different username.")
        finally:
            conn.close()
    
    @staticmethod 
    def del_user(username):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
                "DELETE FROM users WHERE username=?", (username,)
                )
        conn.commit()
        print(f"User '{username}' was deleted.")
        
        if cursor.rowcount == 0:
            print(f"User '{username}' does not exist.")
        else:
            print(f"User '{username}' was deleted.")
        conn.close()
        
# #Example to create user
# admin_user = User("Andy", "1234", is_admin=False)
# admin_user.create_user()


def log_in(username):
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
        cursor.execute(
        "UPDATE users SET isOnline=1 WHERE username =?", (username,)
        
    )
    conn.commit()
    print(f"User '{username}' is logged in")
    conn.close()

    
def log_out(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET isOnline=0 WHERE username =?", (username,)
    )
    conn.commit()
    print(f"User '{username}' is logged out")
    conn.close()


log_in("Admin")
    
            



