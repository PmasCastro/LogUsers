#takes care of user authentication, login, logouts
import sqlite3
import bcrypt

DB_NAME="users.db"

class Authenticator:

    def __init__(self):
        pass

    def online_status(self, username):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT isOnline FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        if result and result[0] == 1:
            print(f"User '{username}' is already logged in")
            conn.close()
            return True
        return False
        
    
    def login(self, username, password):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT password, isOnline FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        
        if result is None:
            print(f"User '{username}' does not exist.")
            conn.close()
            return False
        
        hashed_password, is_online = result

        #Verify password

        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("Invalid password")
            conn.close()
            return False
        if is_online == 1:
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
            return True
    

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
    
    


    
# user_login = Authenticator()

# # # user_login.login("PatoDonald", "122334")

# user_login.logout("PatoDonald")
# user_login.logout("Admin")
# user_login.logout("Pedro")



