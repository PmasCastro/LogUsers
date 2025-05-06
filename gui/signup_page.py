import customtkinter as ctk
import tkinter.messagebox as tkmb
from userdb import User

class SignupPage(ctk.CTkFrame):
    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.configure(width=350, height=400, corner_radius=15, fg_color="#829191")
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.app = app
        

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Create a new account", font=ctk.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username_entry.grid(row=1, column=0, columnspan=2, pady=8)

        self.user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.user_pass.grid(row=2, column=0, columnspan=2, pady=8)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="E-mail", width=250)
        self.email_entry.grid(row=3, column=0, columnspan=2, pady=8)

        self.phone_entry = ctk.CTkEntry(self, placeholder_text="Phone number", width=250)
        self.phone_entry.grid(row=4, column=0, columnspan=2, pady=8)

        self.button = ctk.CTkButton(self, text='Create Account', width=250, command=self.create_account)
        self.button.grid(row=5, column=0, columnspan=2, pady=(20))

    def create_account(self):
        username = self.username_entry.get()
        password = self.user_pass.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        
        user = User(username=username, password=password, email=email, phone=phone)

        if user.create_user():
            tkmb.showinfo("Success", "Account created successfully!")
            # Optionally redirect to login page or main page
            if hasattr(self.app,'load_login_page'):
                self.app.load_login_page()
            else:
                tkmb.showerror("Error", "App instance not found.")