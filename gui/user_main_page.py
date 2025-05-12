import customtkinter as ctk
from auth import Authenticator
import os

class UserMainPage(ctk.CTkFrame):


    def __init__(self, master=None, username=None, user_role=None):

        super().__init__(master)

        #This line sets the username attribute to the username passed to the constructor from the LoginPage.
        #through the App instance on main.py:
        # (def_load_main_page > self.main_page = MainPage(master=self.background_frame,username=username)).
                                                                                  
        self.username = username
        self.user_role = user_role

        self.configure(fg_color="#829191")  # Example background color
        self.grid(row=0, column=0, sticky="nsew")
        self.app = None  
        self.create_widgets()


    def create_widgets(self):

        welcome_text = f"Welcome, {self.username}!" if self.username else "Welcome!"
        self.label = ctk.CTkLabel(self, text=welcome_text, font=ctk.CTkFont(size=24))
        self.label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        test_text = f"Your user role is {self.user_role}"
        self.label = ctk.CTkLabel(self, text=test_text, font=ctk.CTkFont(size=14))
        self.label.grid(row=1, column=0, columnspan=2, pady=(20, 5))

        self.button = ctk.CTkButton(self, text='Logout', width=250, command=self.handle_logout)
        self.button.grid(row=2, column=0, columnspan=2, pady=20)


    def handle_logout(self):

        if self.username:
            auth = Authenticator()
            auth.logout_user(self.username)

            if os.path.exists("session.json"):
                     os.remove("session.json")
            if self.app:
                self.app.load_login_page()