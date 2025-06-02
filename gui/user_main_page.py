import customtkinter as ctk
import tkinter.messagebox as tkmb
from CTkTable import *
from auth import Authenticator
from management import UserManagement
from datetime import datetime
import pytz
import sqlite3
import os

DB_NAME = "users.db"
lisbon = pytz.timezone("Europe/Lisbon")


class UserMainPage(ctk.CTkFrame):

    def __init__(self, master=None, username=None, user_role=None, app = None):
        super().__init__(master)
        self.username = username
        self.user_role = user_role
        self.app = app

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
        ctk.CTkButton(self.navbar, text="Settings", command=self.show_settings).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(self.navbar, text="Logout", command=self.handle_logout).grid(row=0, column=2, padx=10, pady=10)

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

        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT username, user_id, event, timestamp FROM login WHERE username = ?",
                    (self.username,)
                )
                rows = cursor.fetchall()
        except sqlite3.OperationalError:
            print("Database error occurred.")
            rows = []

        headers = ["Username", "User ID", "Event", "Timestamp"]

        scroll_frame = ctk.CTkScrollableFrame(self.content_frame, fg_color="#3e3e42", corner_radius=20)
        scroll_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Add headers
        for col_index, header in enumerate(headers):
            header_label = ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 14, "bold"), text_color="white")
            header_label.grid(row=0, column=col_index, padx=10, pady=5)

        # Add data rows
        for row_index, user in enumerate(rows, start=1):
            for col_index, item in enumerate(user):
                # Convert UTC timestamp to Lisbon time (if timestamp column)
                if col_index == 3 and isinstance(item, str):
                    try:
                        utc_time = datetime.strptime(item, "%Y-%m-%d %H:%M:%S")
                        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(lisbon)
                        item = local_time.strftime("%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        pass

                label = ctk.CTkLabel(
                    scroll_frame,
                    text=str(item),
                    font=("Arial", 14),
                    text_color="white",
                    width=150,
                    )
                
                if col_index == 0:
                    label._label.configure(anchor="w")  # Left-align Username
                elif col_index == 1:
                    label._label.configure(anchor="center")  # Center-align User ID
                elif col_index == 2:
                    label._label.configure(anchor="w")  # Center-align Event
                elif col_index == 3:
                    label._label.configure(anchor="e")  # Right-align Timestamp

                label.grid(row=row_index, column=col_index, padx=30, pady=5)

    def show_settings(self):

        self.clear_content_frame()

        frame = ctk.CTkFrame(self.content_frame, fg_color="#3e3e42", corner_radius=20)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        frame.grid_columnconfigure(0, weight=1)

    # Add title label (correctly now!)
        title_label = ctk.CTkLabel(frame, text="Settings Panel", font=("Arial", 20), text_color="white")
        title_label.pack(pady=(10, 20))

        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT username, email, phone FROM users WHERE username = ?", (self.username,))

                user_data = cursor.fetchone()

        except sqlite3.OperationalError as e:
            print("Database error occurred.", e)
            user_data = ("", "", "")
        
        current_username, email, phone = user_data if user_data else ("", "", "")
            
        self.username_entry = ctk.CTkEntry(frame, placeholder_text="New Username", width=250)
        self.email_entry = ctk.CTkEntry(frame, placeholder_text="New Email", width=250)
        self.phone_entry = ctk.CTkEntry(frame, placeholder_text="New Phone", width=250)
        save_button = ctk.CTkButton(frame, text="Save Changes", command=self.save_changes)

        self.username_entry.insert(0, current_username)
        self.email_entry.insert(0, email)
        self.phone_entry.insert(0, phone)
        
        self.username_entry.pack(pady=10)
        self.email_entry.pack(pady=10)
        self.phone_entry.pack(pady=10)
        save_button.pack(pady=20)
        
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


    def save_changes(self):

        self.new_username = self.username_entry.get().strip()
        self.new_email = self.email_entry.get().strip()
        self.new_phone = self.phone_entry.get().strip()

        user_management = UserManagement()

        try:
            user_management.change_username(self.username, self.new_username)
            user_management.change_email(self.new_username, self.new_email)
            user_management.change_phone(self.new_username, self.new_phone)

            tkmb.showinfo("Success", "Changes saved successfully!")
            self.username = self.new_username  # Update the username in the instance

            if self.app:
                self.app.logged_in_username = self.new_username

            self.show_settings()  # Refresh the settings page

        except ValueError as e:
            if "already exists" in str(e):
                tkmb.showerror("Error", "Username or email already exists.")
            

    def handle_logout(self):

        username_to_logoout = self.new_username if hasattr(self, 'new_username') else self.username
        
        if username_to_logoout:
            
            auth = Authenticator()
            auth.logout_user(username_to_logoout)

            if os.path.exists("session.json"):
                os.remove("session.json")

            if self.app:
                self.app.load_login_page()
