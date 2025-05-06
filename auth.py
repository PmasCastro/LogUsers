#takes care of user authentication, login, logouts
import sqlite3
import bcrypt

DB_NAME="users.db"

class Authenticator:

    def __init__(self):
        pass

    # def online_status(self, username):
    #     conn = sqlite3.connect(DB_NAME)
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT isOnline FROM users WHERE username=?", (username,))
    #     result = cursor.fetchone()
    #     if result and result[0] == 1:
    #         print(f"User '{username}' is already logged in")
    #         conn.close()
    #         return True
    #     return False
        
    def authenticate_user(self, username, password):
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, password, isOnline FROM users WHERE username=?", (username,))
                result = cursor.fetchone()
                
                if result is None:
                    raise ValueError("User does not exist.")
                    
                user_id, hashed_password, is_online = result
                
                if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    raise ValueError("Password is incorrect.")
                
                if is_online == 1:
                    raise ValueError("User is already logged in.")
                
                cursor.execute("UPDATE users SET isOnline=1 WHERE username = ?", (username,))
                cursor.execute(
                    "INSERT INTO login (username, user_id, event) VALUES (?, ?, ?)",
                    (username, user_id, "login")
                    )
                print("User logged in successfully")
                conn.commit()

                return True
        finally:
            conn.close()

    def logout_user(self, username):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        
        user = cursor.fetchone()
        
        if user:
            user_id = user[0]
            cursor.execute("UPDATE users SET isOnline=0 WHERE username=?", (username,))
            cursor.execute("INSERT INTO login (username, user_id, event) VALUES (?, ?, ?)",
                       (username, user_id, "logout"))
            conn.commit()
            conn.close()
    
    


    
# user_login = Authenticator()

#  # user_login.login("PatoDonald", "122334")

# user_login.logout("PatoDonald")
# user_login.logout("Admin")
# user_login.logout("Pedro")



