#This file only handles db interactions: connects the db on init; adds new users; checks if user exists etc
import sqlite3
import bcrypt

DB_NAME = "users.db"

class User:
    def __init__(self, username, password, email, phone, is_admin=False):
        
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.is_admin=is_admin
        
    #Add new user to db
    def create_user(self):

        if not all(field.strip() for field in [self.username, self.password, self.email, self.phone]):
            print("Please fill in all fields")
            return

        
        #encrypt the password
        hashed = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            if "@" not in self.email or "." not in self.email:
                    print("Invalid email format.")
                    return
            else:
                #VALUES placeholder (?, ?, ?, ?) prevents SQL injection
                cursor.execute(
                "INSERT INTO users (username, password, email, phone, isOnline, isAdmin) VALUES (?, ?, ?, ?, ?, ?)", 
                (self.username, hashed, self.email, self.phone,  0, int(self.is_admin))
                )
            conn.commit()
            print(f"User '{self.username}' created successfully.")

        #If user already exists, print message and return
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
# admin_user = User("", "1234", "2@gmail.com", " 2", is_admin=False)
# admin_user.create_user()

#Delete user
# User.del_user("Castro")





            

