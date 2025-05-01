## Login Page using customtkinter

import customtkinter as ctk 
import tkinter.messagebox as tkmb
# from auth import Authenticator


ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("400x400") 
app.title("Login Page")


class LoginPage(ctk.CTkFrame): 
    def __init__(self, master=None): 
        super().__init__(master) 
        self.master = master 
        self.create_widgets() 
  
    def create_widgets(self): 
        self.label = ctk.CTkLabel(self, text="Login Page") 
        self.label.pack(pady=20) 
  
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Username") 
        self.user_entry.pack(pady=12, padx=10)
  
        self.user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*") 
        self.user_pass.pack(pady=12, padx=10) 
  
        self.button = ctk.CTkButton(self, text='Login', command=self.login) 
        self.button.pack(pady=12, padx=10) 
  
    def login(self): 
        username = self.user_entry.get() 
        password = self.user_pass.get() 
        if username == "" or password == "": 
            tkmb.showerror("Error", "Please fill in all fields") 
            return
        
    
  
login_page = LoginPage(master=app)
login_page.pack(fill="both", expand=True)
  
app.mainloop()