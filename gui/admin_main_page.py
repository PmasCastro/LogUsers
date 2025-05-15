import customtkinter as ctk
from CTkTable import *
from auth import Authenticator
import sqlite3
import os

DB_NAME = "users.db"

class AdminMainPage(ctk.CTkFrame):
    def __init__(self, master=None, username=None, user_role=None):
        super().__init__(master)
        self.username = username
        self.user_role = user_role

        self.configure(fg_color="#1e1e1e")
        self.grid(row=0, column=0, sticky="nsew")

        # Grid layout for AdminMainPage
        self.grid_rowconfigure(0, weight=0)  # Navbar row (fixed height)
        self.grid_rowconfigure(1, weight=1)  # Content row (expandable)
        self.grid_columnconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # === NAVBAR ===
        self.navbar = ctk.CTkFrame(self, fg_color="#3e3e42", height=200, corner_radius=0)
        self.navbar.grid(row=0, column=0, sticky="ew")  # full width
        self.navbar.grid_columnconfigure((0,1,2,3), weight=1)  # evenly distribute buttons

        ctk.CTkButton(self.navbar, text="Dashboard").grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkButton(self.navbar, text="Users").grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkButton(self.navbar, text="Settings").grid(row=0, column=2, padx=10, pady=5)
        ctk.CTkButton(self.navbar, text="Logout", command=self.handle_logout).grid(row=0, column=3, padx=10, pady=5)

        # === CONTENT AREA ===
        self.content_frame = ctk.CTkFrame(self, fg_color="#3e3e42", corner_radius=20)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=60, pady=60) #with padx and pady you can resize the content area size
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # === Users table ===

        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT id, username, email, phone, isOnline, isAdmin FROM users")

                rows = cursor.fetchall()

                headers = ["User ID", "Username", "Email", "Phone Number", "Online", "Role"]

                data = [headers] + rows

        except sqlite3.OperationalError:
            print("Database error occurred. Please check the database connection")
          
        table = CTkTable(self.content_frame, row=5, column=5, values=data)
        table.pack(expand=False, fill="both", padx=30, pady=30)

    def handle_logout(self):
        if self.username:
            auth = Authenticator()
            auth.logout_user(self.username)

            if os.path.exists("session.json"):
                os.remove("session.json")

            if self.app:
                self.app.load_login_page()