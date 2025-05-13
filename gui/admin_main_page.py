import customtkinter as ctk
from auth import Authenticator
import os

class AdminMainPage(ctk.CTkFrame):
    def __init__(self, master=None, username=None, user_role=None):
        super().__init__(master)
        self.username = username
        self.user_role = user_role

        self.configure(fg_color="#829191")
        self.grid(row=0, column=0, sticky="nsew")

        # Grid layout for AdminMainPage
        self.grid_rowconfigure(0, weight=0)  # Navbar row (fixed height)
        self.grid_rowconfigure(1, weight=1)  # Content row (expandable)
        self.grid_columnconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # === NAVBAR ===
        self.navbar = ctk.CTkFrame(self, fg_color="#317AC1", height=100, corner_radius=0)
        self.navbar.grid(row=0, column=0, sticky="ew")  # full width
        self.navbar.grid_columnconfigure((0,1,2,3), weight=1)  # evenly distribute buttons

        ctk.CTkButton(self.navbar, text="Dashboard").grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkButton(self.navbar, text="Users").grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkButton(self.navbar, text="Settings").grid(row=0, column=2, padx=10, pady=5)
        ctk.CTkButton(self.navbar, text="Logout", command=self.handle_logout).grid(row=0, column=3, padx=10, pady=5)

        # === CONTENT AREA ===
        self.content_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=20)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        placeholder = ctk.CTkLabel(self.content_frame, text="Table Placeholder", text_color="black")
        placeholder.grid(row=0, column=0)

    def handle_logout(self):
        if self.username:
            auth = Authenticator()
            auth.logout_user(self.username)

            if os.path.exists("session.json"):
                os.remove("session.json")

            if self.app:
                self.app.load_login_page()