from userdb import User


#This function handles inputs from GUI, receives username and password and creates user on db
def create_new_user(username_entry, password_entry):
    
    username = username_entry.get()
    password = password_entry.get()

    if password and username:
        user = User(username, password)
        user.create_user()
    else:
        print("Please fill in both fields.")
    








