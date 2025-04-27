import sqlite3

DB_NAME = "users.db"

class UserManagement:
    def __init__(self):
        pass

    def change_username(self, old_username, new_username):
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            # Check if the old_username exists in the database

            cursor.execute(
                "SELECT username FROM users WHERE username=?", (old_username,))
            result = cursor.fetchone()

            # If the old_username does not exist, print a message and return

            if result is None:
                print(f"User '{old_username}' does not exist.")
                return
            else:
                cursor.execute(
                    "SELECT username FROM users WHERE username=?", (new_username,))

                result = cursor.fetchone()
                if result is not None:
                    print(f"User '{new_username}' already exists, please choose a different username.")
                    return
                else:
                    cursor.execute(
                        "UPDATE users SET username=? WHERE username=?", (new_username, old_username))

                    conn.commit()
                    print(f"User '{old_username}' changed to '{new_username}' successfully.")
            
        
        
            
        finally:
            conn.close()

        
           

            
                


      








    def change_password():
        pass

    def change_email():
        pass

    def change_phone():
        pass

    def change_status():
        pass


manager = UserManagement()
manager.change_username("Admin2", "Admin")
        

 