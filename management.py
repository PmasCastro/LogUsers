import sqlite3
import bcrypt

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
            
            # If the old_username exists, check if the new_username already exists
            else:
                cursor.execute(
                    "SELECT username FROM users WHERE username=?", (new_username,))
                result = cursor.fetchone()
            
            # If the new_username already exists, print a message and return
                if result is not None:
                    print(f"User '{new_username}' already exists, please choose a different username.")
                    return
                if " " in new_username:
                    print("Username cannot contain spaces.")
                    return
                
            # If the new_username does not exist, update the username    
                else:
                    cursor.execute(
                        "UPDATE users SET username=? WHERE username=?", (new_username, old_username))
                    conn.commit()
                    print(f"User '{old_username}' changed to '{new_username}' successfully.")
        finally:
            conn.close()
    
    def change_password(self, username, old_password, new_password):

        #Need to refactor to check the old password before changing it

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            # Check if the username exists in the database
            cursor.execute(
                "SELECT password FROM users WHERE username=?", (username,))
            result = cursor.fetchone()

            # If the username does not exist, print a message and return
            if result is None:
                print(f"User '{username}' does not exist.")
                return
            
            stored_password = result[0]

            if not bcrypt.checkpw(old_password.encode('utf-8'), stored_password):
                raise ValueError("Old password is incorrect.")
            
            # if len(new_password) < 8:

            if " " in new_password:
                raise ValueError("Password cannot contain spaces.")
            
            hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute(
                "UPDATE users SET password=? WHERE username=?", (hashed, username))
            conn.commit()
            
        finally:
            conn.close()
            print(f"Password for user '{username}' changed successfully.")
        

    def change_email(self, username, new_email):

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            if " " in new_email:
                raise ValueError("Email cannot contain spaces.")
            
            if "@" not in new_email or "." not in new_email:
                raise ValueError("Invalid email format.")
            
            cursor.execute(
                "SELECT email FROM users WHERE username=?", (username,))
            result = cursor.fetchone()

            if result is None:
                raise ValueError(f"User '{username}' does not exist.")
            
            current_email = result[0]

            if new_email == current_email:
                raise ValueError("New email cannot be the same as the current email.")
            
            cursor.execute(
                "SELECT 1 FROM users WHERE email=?", (new_email,))
            if cursor.fetchone():
                raise ValueError("Email already assigned to a different account.")
            
            cursor.execute(
                "UPDATE users SET email=? WHERE username=?", (new_email, username))
            conn.commit()
            print(f"Email for user '{username}' changed successfully to '{new_email}'.")
           
        finally:
            conn.close()

          
    def change_phone(self, username, new_phone):

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            new_phone = new_phone.strip()

            if not new_phone.isdigit():
                raise ValueError("Phone number must contain only digits.")
            
            if len(new_phone) != 9:
                raise ValueError("Phone number must be 9 digits long.")
            

            cursor.execute(
                "SELECT phone FROM users WHERE username=?", (username,))
            result = cursor.fetchone()

            if result is None:
                raise ValueError(f"User '{username}' does not exist.")
            
            current_phone = result[0]

            if new_phone == current_phone:
                raise ValueError("New phone number cannot be the same as the current phone number.")
            

            cursor.execute(
                "SELECT 1 FROM users WHERE phone=?", (new_phone,))
            if cursor.fetchone():
                raise ValueError("Phone number already assigned to a different account.")
            
            
            cursor.execute(
                "UPDATE users SET phone=? WHERE username=?", (new_phone, username))
            conn.commit()
            print(f"Phone number for user '{username}' changed successfully to '{new_phone}'.")
        
        finally:
            conn.close()

    def change_status(self, username, make_admin: int):

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            if make_admin not in (0, 1):
                raise ValueError("Invalid value for make_admin. Use 0 for regular user and 1 for admin.")

            cursor.execute(
                "SELECT isAdmin FROM users WHERE username=?", (username,))
            
            result = cursor.fetchone()

            if result is None:
                raise ValueError(f"User '{username}' does not exist.")
            
            current_status = result[0]

            if make_admin == current_status:
                raise ValueError(f"User '{username}' is already {'an admin' if make_admin == 1 else 'a regular user'}.")

            if current_status != make_admin:
                cursor.execute(
                    "UPDATE users SET isAdmin=? WHERE username=?", (make_admin, username))
                conn.commit()
                if make_admin == 1:
                    print(f"User '{username}' is now an admin.")
                else:
                    print(f"User '{username}' is no longer an admin.")

        finally:
            conn.close()  
    
    # This function updates user fields such as username, email, and phone. It's flexible
    # the user can choose to update any combination of these fields.
    def update_user_fields(self, current_username, new_username=None, new_email=None, new_phone=None):
        #we pass current_username to identify the user we want to update

        # updates: a list that will hold SQL snippets like "username = ?". - which column to update.
        # params: values to go in place of those ? placeholders in the SQL query. We use this to prevent SQL injection.
        updates = []
        params = []

        if new_username:
            updates.append("username=?")
            params.append(new_username)
        if new_email:
            updates.append("email=?")
            params.append(new_email)
        if new_phone:
            updates.append("phone=?")
            params.append(new_phone)
        if not updates:
            print("No fields to update.")
            return
        
        params.append(current_username)
        query = f"UPDATE users SET {', '.join(updates)} WHERE username=?"

        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
        except sqlite3.Error as e:
            print("Update failed:", e)

       
        


        

# mg = UserManagement()

# mg.change_password("Admin", "1234", "123")