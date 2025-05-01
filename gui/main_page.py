import customtkinter as ctk

class MainPage(ctk.CTkFrame):
    def __init__(self, master=None, username=None):
        super().__init__(master)
        self.username = username
        self.configure(fg_color="white")  # Example background color
        self.grid(row=0, column=0, sticky="nsew")
        self.app = None  
        self.create_widgets()


    
    def create_widgets(self):
        welcome_text = f"Welcome, {self.username}!" if self.username else "Welcome!"
        self.label = ctk.CTkLabel(self, text=welcome_text, font=ctk.CTkFont(size=24))
        self.label.pack(pady=50)
