# from userdb import User
# from tkinter import messagebox, END

# #This function handles inputs from GUI, receives username and password and creates user on db
# def create_new_user(username_entry, password_entry):
    
#     username = username_entry.get()
#     password = password_entry.get()

#     if password and username:
#         user = User(username, password)
#         user.create_user()
#         messagebox.showinfo("", "User created successfully")
#         username_entry.delete(0, END)
#         password_entry.delete(0, END)
#     else:
#         messagebox.showwarning("Warning", "Please fill in both fields")