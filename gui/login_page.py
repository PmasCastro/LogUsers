## Login Page using customtkinter
from auth import Authenticator 
import customtkinter as ctk 
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("light")  # Or 'dark' for dark mode
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("600x500") 
app.title("Login Page")

# Configure main window grid to center the login frame
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Outer frame with background color
background_frame = ctk.CTkFrame(app, fg_color="#4C5B61")
background_frame.grid(row=0, column=0, sticky="nsew")

background_frame.grid_rowconfigure(0, weight=1)
background_frame.grid_columnconfigure(0, weight=1)


class LoginPage(ctk.CTkFrame): 
    def __init__(self, master=None): 
        super().__init__(master)
        self.configure(width=350, height=400, corner_radius=15, fg_color="#829191")
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        self.create_widgets()

    def create_widgets(self): 
        self.label = ctk.CTkLabel(self, text="Sign in to your account", font=ctk.CTkFont(size=18, weight="bold")) 
        self.label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.signup_label = ctk.CTkLabel(self, text="or create account", text_color="blue", cursor="hand2", font=ctk.CTkFont(size=12, underline=True))
        self.signup_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        self.signup_label.bind("<Button-1>", lambda e: tkmb.showinfo("Redirect", "Redirecting to sign up"))

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250) 
        self.username_entry.grid(row=2, column=0, columnspan=2, pady=8)

        self.user_pass = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250) 
        self.user_pass.grid(row=3, column=0, columnspan=2, pady=8)

        self.remember = ctk.CTkCheckBox(self, text="Remember me") 
        self.remember.grid(row=4, column=0, sticky="w", padx=48)

        self.forgot = ctk.CTkLabel(self, text="Forgot your password?", text_color="blue", cursor="hand2", font=ctk.CTkFont(size=12, underline=True))
        self.forgot.grid(row=4, column=1, sticky="e", padx=8)
        self.forgot.bind("<Button-1>", lambda e: tkmb.showinfo("Reset", "Redirecting to password reset"))

        self.button = ctk.CTkButton(self, text='Sign in', width=250, command=self.login) 
        self.button.grid(row=5, column=0, columnspan=2, pady=20)

    def login(self): 
        username = self.username_entry.get() 
        password = self.user_pass.get() 
        if username == "" or password == "": 
            tkmb.showerror("Error", "Please fill in all fields") 
            return
        else:
            auth = Authenticator()
            if auth.login(username, password):
                tkmb.showinfo("Success", "Login successful")
                # Redirect to main application or dashboard
            else:
                tkmb.showerror("Error", "Invalid username or password")
           
login_page = LoginPage(master=background_frame)

app.mainloop()