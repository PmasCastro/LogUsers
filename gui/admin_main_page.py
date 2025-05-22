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

        self.grid_rowconfigure(0, weight=0)  # Navbar
        self.grid_rowconfigure(1, weight=1)  # Content
        self.grid_columnconfigure(0, weight=1)

        self.create_widgets()
        self.show_dashboard()


    def create_widgets(self):
        # === NAVBAR ===
        self.navbar = ctk.CTkFrame(self, fg_color="#3e3e42", height=60, corner_radius=0)
        self.navbar.grid(row=0, column=0, sticky="ew")
        self.navbar.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkButton(self.navbar, text="Dashboard", command=self.show_dashboard).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(self.navbar, text="Users", command=self.show_users).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(self.navbar, text="Settings", command=self.show_settings).grid(row=0, column=2, padx=10, pady=10)
        ctk.CTkButton(self.navbar, text="Logout", command=self.handle_logout).grid(row=0, column=3, padx=10, pady=10)

        # === CONTENT AREA ===
        self.content_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=20)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=40)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)


    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


    def show_dashboard(self):
        self.clear_content_frame()
        frame = ctk.CTkFrame(self.content_frame, fg_color="#3e3e42", corner_radius=20)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        label = ctk.CTkLabel(frame, text="Dashboard View", font=("Arial", 20), text_color="white")
        label.pack(pady=20)
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, email, phone, isOnline, isAdmin FROM users")
                rows = cursor.fetchall()
                headers = ["User ID", "Username", "Email", "Phone Number", "Online", "Role"]
                data = [headers] + rows
            
        except sqlite3.OperationalError:
            print("Database error occurred. Please check the database connection")
            data = [["Error loading data"]]
        
        table = CTkTable(frame, values=data)  # Removed invalid row=5, column=5
        table.pack(expand=True, fill="both", padx=60, pady=60)

        #  === Users table ===


    def show_settings(self):
        self.clear_content_frame()
        frame = ctk.CTkFrame(self.content_frame, fg_color="#3e3e42", corner_radius=20)
        label = ctk.CTkLabel(frame, text="Settings Panel", font=("Arial", 20), text_color="White")
        label.pack(pady=20)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


    def show_users(self):
        self.clear_content_frame()
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, email, phone, isOnline, isAdmin FROM users")
                rows = cursor.fetchall()
        except sqlite3.OperationalError:
            print("Database error occurred.")
            rows = []

        headers = ["User ID", "Username", "Email", "Phone", "Online", "Role", "Action"]

        scroll_frame = ctk.CTkScrollableFrame(self.content_frame, fg_color="#3e3e42", corner_radius=20)
        scroll_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Header
        for col_index, header in enumerate(headers):
            label = ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 18, "bold"), text_color="white")
            label.grid(row=0, column=col_index, padx=10, pady=5)

        # Data rows
        for row_index, user in enumerate(rows, start=1):
            for col_index, item in enumerate(user):
                label = ctk.CTkLabel(scroll_frame, text=str(item), font=("Arial", 14), text_color="white")
                label.grid(row=row_index, column=col_index, padx=10, pady=5)

            is_online = user[4]
            username = user[1]

            if is_online:
                logout_button = ctk.CTkButton(
                    scroll_frame,
                    text="Log Out",
                    width=80,
                    command=lambda u=username: self.force_logout_user(u)
                )
                logout_button.grid(row=row_index, column=len(user), padx=10, pady=5)


    def handle_logout(self):
        if self.username:
            auth = Authenticator()
            auth.logout_user(self.username)

            if os.path.exists("session.json"):
                os.remove("session.json")

            if self.app:
                self.app.load_login_page()


    def force_logout_user(self, username):
        auth = Authenticator()
        auth.logout_user(username)

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET isOnline = 0 WHERE username = ?", (username,))
            conn.commit()

        self.show_users()
