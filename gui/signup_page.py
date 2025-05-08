import customtkinter as ctk
import tkinter.messagebox as tkmb
from userdb import User

class SignupPage(ctk.CTkFrame):
    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.app = app
        self.configure(width=350, height=400, corner_radius=15, fg_color="#829191")
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.columnconfigure((0, 1), weight=1)
        
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Create a new account", font=ctk.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.turn_back_btn = ctk.CTkButton(self, text='Back to login', width=150, command=lambda: self.app.load_login_page())
        self.turn_back_btn.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username_entry.grid(row=2, column=0, columnspan=2, pady=8)

        self.user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.user_pass.grid(row=3, column=0, columnspan=2, pady=8)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="E-mail", width=250)
        self.email_entry.grid(row=4, column=0, columnspan=2, pady=8)

        self.phone_entry = ctk.CTkEntry(self, placeholder_text="Phone number", width=250)
        self.phone_entry.grid(row=5, column=0, columnspan=2, pady=8)

        self.button = ctk.CTkButton(self, text='Create Account', width=250, command=self.handle_user_registration)
        self.button.grid(row=6, column=0, columnspan=2, pady=(20))

    def handle_user_registration(self):

        username = self.username_entry.get()
        password = self.user_pass.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not username or not password or not email or not phone:
            tkmb.showerror("Error", "All fields are required!")
            return

        user = User(username=username, password=password, email=email, phone=phone)

        

        user.register_user()


        

        
    
        
        # Check if the user was created successfully
        tkmb.showinfo("Success", "Account created successfully!")

        if self.app:
            self.app.load_login_page()

    



        