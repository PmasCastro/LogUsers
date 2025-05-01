import customtkinter as ctk

class MainPage(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(fg_color="white")  # Example background color
        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Welcome to the Main Page!", font=ctk.CTkFont(size=24))
        self.label.pack(pady=50)
