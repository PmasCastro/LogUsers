## Login Page using customtkinter
from auth import Authenticator
import customtkinter as ctk
import tkinter.messagebox as tkmb
import json
import os

ctk.set_appearance_mode("light")  # Or 'dark' for dark mode
ctk.set_default_color_theme("blue")

class LoginPage(ctk.CTkFrame):
    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.app = app
        self.configure(width=350, height=400, corner_radius=15, fg_color="#829191")
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        

        #remember_var is a BooleanVar that will be used to store the state of the "Remember me" checkbox.
        #It is initialized to False, meaning the checkbox is not checked by default.
        #Without this, the checkbox will not be able to store its state.
        self.remember_var = ctk.BooleanVar()
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Sign in to your account", font=ctk.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.signup_label = ctk.CTkLabel(self, text="or create account", text_color="blue", cursor="hand2", font=ctk.CTkFont(size=12, underline=True))
        self.signup_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        self.signup_label.bind("<Button-1>", lambda e: self.app.load_signup_page())

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username_entry.grid(row=2, column=0, columnspan=2, pady=8)

        self.user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.user_pass.grid(row=3, column=0, columnspan=2, pady=8)

        self.remember = ctk.CTkCheckBox(self, text="Remember me", variable=self.remember_var)
        self.remember.grid(row=4, column=0, sticky="w", padx=48)

        self.forgot = ctk.CTkLabel(self, text="Forgot your password?", text_color="blue", cursor="hand2", font=ctk.CTkFont(size=12, underline=True))
        self.forgot.grid(row=4, column=1, sticky="e", padx=8)
        self.forgot.bind("<Button-1>", lambda e: tkmb.showinfo("Reset", "Redirecting to password reset"))

        self.button = ctk.CTkButton(self, text='Sign in', width=250, command=self.login)
        self.button.grid(row=5, column=0, columnspan=2, pady=20)

    def login(self):
        # Check if the username and password fields are empty
        username = self.username_entry.get()
        password = self.user_pass.get()

        try:
            if not username.strip() or not password.strip():
                raise ValueError("Please fill in all fields")
        except ValueError as e:
            tkmb.showerror("Error", str(e))
            return
        
        auth = Authenticator()

        try:
            if auth.login(username, password):
                tkmb.showinfo("Success", "Login successful")
                if self.remember_var.get():                    
                    
                    # Store the username in a json file
                    with open("session.json", "w") as f:
                        json.dump({"username": username, "remember_me": True}, f)
                else:
                    if os.path.exists("session.json"):
                        os.remove("session.json")

                if self.app:
                    self.app.remember_var.set(self.remember_var.get())

                #Store the username in the app instance for later use
                self.app.logged_in_username = username
                self.app.load_main_page(username)

        except ValueError as e: 
            if str(e) == "User does not exist.":
                tkmb.showerror("Error", "User does not exist")
            elif str(e) == "Password is incorrect.":
                tkmb.showerror("Error", "Password is incorrect")
            elif str(e) == "User is already logged in.":
                tkmb.showerror("Error", "User is already logged in")
            return

        
                
    
        