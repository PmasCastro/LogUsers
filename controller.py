from app import *
from userdb import User

def create_new_user():
    from app import username_entry, password_entry
    

    username = username_entry.get()
    password = password_entry.get()

    if password and username:
        user = User(username, password)
        user.create_user()
    else:
        print("Please fill in both fields.")







