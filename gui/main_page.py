import customtkinter as ctk 
# import tkinter.messagebox as tkmb

class MainUI(ctk.CTkFrame):
    def __init__(self, master=None, username=""):
        super().__init__(master)
        self.configure(width=600, height=500)
        self.grid(row=0, column=0)
        
        # Add the "Hello" message
        self.label = ctk.CTkLabel(self, text=f"Hello, {username}!", font=ctk.CTkFont(size=18))
        self.label.grid(row=0, column=0, pady=20)