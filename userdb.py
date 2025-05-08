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
    
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        return len(phone) == 9 and phone.isdigit()
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email
    
    #Add new user to db
    def register_user(self):

        if not User.is_valid_email(self.email):
            print("Invalid email format.")
            return
        if not User.is_valid_phone(self.phone):
            print("Invalid phone number format.")
            return

        #encrypt the password
        hashed = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()

                #VALUES placeholder (?, ?, ?, ?) prevents SQL injection
                cursor.execute(
                "INSERT INTO users (username, password, email, phone, isOnline, isAdmin) VALUES (?, ?, ?, ?, ?, ?)", 
                (self.username, hashed, self.email, self.phone,  0, int(self.is_admin))
                )
                
                conn.commit()
                print(f"User '{self.username}' created successfully.")

        except sqlite3.IntegrityError as e:
            if 'username' in str(e):
                raise ValueError("Username already exists.")
            elif 'email' in str(e):
                raise ValueError("Email already assigned to a different account.")
            elif 'phone' in str(e):
                raise ValueError("Phone number already assigned to a different account.")
            else:
                raise ValueError(f"An error occurred: {e}")    
            
        except sqlite3.OperationalError:
            print("Database error occurred. Please check the database connection.")
    
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
# admin_user = User("Test", "1234", "test@gmail.com", "965448951", is_admin=False)
# admin_user.register_user()






            

