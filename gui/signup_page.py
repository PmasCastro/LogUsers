import customtkinter as ctk
import tkinter.messagebox as tkmb
from userdb import User

def limit_phone_input(input_str, current_value):
    # current_value already includes input_str, so just check its length
    if input_str == "" or (input_str.isdigit() and len(current_value) <= 9):
        return True
    return False


class SignupPage(ctk.CTkFrame):
    
    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.app = app
        self.configure(width=350, height=500, corner_radius=15, fg_color="#829191")
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.columnconfigure((0, 1), weight=1)

        self.vcmd = (self.register(limit_phone_input), '%S', '%P')
        
        self.create_widgets()

    def create_widgets(self):

        #Header label
        self.label = ctk.CTkLabel(self, text="Create a new account", font=ctk.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.turn_back_btn = ctk.CTkButton(self, text='Back to login', width=150, command=lambda: self.app.load_login_page())
        self.turn_back_btn.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        #Username label and entry
        self.username_label = ctk.CTkLabel(self, text="Username", font=ctk.CTkFont(size=14, weight="bold"))
        self.username_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=50, pady=(2, 0))

        self.username_entry = ctk.CTkEntry(self, width=250)
        self.username_entry.grid(row=3, column=0, columnspan=2, pady=2)

        #Password label and entry
        self.password_label = ctk.CTkLabel(self, text="Password", font=ctk.CTkFont(size=14, weight="bold"))
        self.password_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=50, pady=(2, 0))

        self.password = ctk.CTkEntry(self, show="*", width=250)
        self.password.grid(row=5, column=0, columnspan=2, pady=2)
        
        #Email label and entry
        self.email_label = ctk.CTkLabel(self, text="Email", font=ctk.CTkFont(size=14, weight="bold"))
        self.email_label.grid(row=6, column=0, columnspan=2, sticky="w", padx=50, pady=(2, 0))

        self.email_entry = ctk.CTkEntry(self, width=250)
        self.email_entry.grid(row=7, column=0, columnspan=2, pady=2)

        #Phone number label and entry
        self.phone_label = ctk.CTkLabel(self, text="Phone number", font=ctk.CTkFont(size=14, weight="bold"))
        self.phone_label.grid(row=8, column=0, columnspan=2, sticky="w", padx=50, pady=(2, 0))

        self.phone_entry = ctk.CTkEntry(self, placeholder_text= "Phone number", width=250, validate="key", validatecommand=self.vcmd)
        self.phone_entry.grid(row=9, column=0, columnspan=2, pady=2)
        
        #Signup button
        self.button = ctk.CTkButton(self, text='Create Account', width=250, command=self.handle_user_registration)
        self.button.grid(row=10, column=0, columnspan=2, pady=(20))

    def handle_user_registration(self):

        username = self.username_entry.get()
        password = self.password.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not username or not password or not email or not phone:
            tkmb.showerror("Error", "All fields are required!")
            return
        if len(phone) !=9:
            tkmb.showerror("Error", "Phone number must be 9 digits long.")
            return

        user = User(username=username, password=password, email=email, phone=phone)

        try:
            if user.register_user():
                tkmb.showinfo("Success", "Account created successfully!")
                
        except ValueError as e: 
            if 'username' in str(e):
                tkmb.showerror("Error", "Username already exists.")
            elif 'email' in str(e):
                tkmb.showerror("Error", "Email already assigned to a different account.")
            elif 'phone' in str(e):
                tkmb.showerror("Error", "Phone number already assigned to a different account.")
            else:
                tkmb.showerror("Error", f"An error occurred: {e}")
            return
        
        finally:
            if self.app:
                self.app.load_login_page()
        

    



        


        

        
    
        

        

    



        