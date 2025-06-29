# This is the main entry point for the application. It initializes the GUI and starts the main loop.
# It also handles the flow of the app, including managing the flow between different pages.

#Data flow management: Now the App and LoginPage share the remember_var
#allowing the app to properly handle user session persistence
#(e.g., saving/loading the "Remember me" state in session.json).

from gui.signup_page import SignupPage
from gui.login_page import LoginPage
from gui.user_main_page import UserMainPage
from gui.admin_main_page import AdminMainPage
import customtkinter as ctk
from auth import Authenticator
import os
import json

class App(ctk.CTk):

    #Sets up the different pages' geometry
    def __init__(self):

        super().__init__()
        self.geometry("1200x850")
        self.title("Login App")
        
        #Initialize state variables
        self.remember_var = ctk.BooleanVar(value=False)  
        self.logged_in_username = None
        self.user_role = None
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Configure grid for the main window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Outer frame with background color
        self.background_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=0) 
        self.background_frame.grid(row=0, column=0, sticky="nsew")
        self.background_frame.grid_rowconfigure(0, weight=1)
        self.background_frame.grid_columnconfigure(0, weight=1)
        
        #Initialize current page tracking
        self.current_page = None 
        
        self.load_session()

        if not self.logged_in_username:
            #If the user is not logged in, load the login page
            self.load_login_page()
        
    def load_session(self):

        session_file = "session.json"

        if os.path.exists(session_file):

            with open(session_file, "r") as f:
                session_data = json.load(f)

                if session_data.get("remember_me"):

                    username = session_data.get("username")
                    user_role = session_data.get("role")
                    #Set the remember_var to True if the checkbox was checked
                    #This ensures that the checkbox state is consistent if the user never loggs out and closes the app.
                    self.remember_var.set(True)
                    self.logged_in_username = username
                    self.user_role = user_role

                    if self.user_role == "admin":
                        self.load_admin_page(username, user_role)
                    else:
                        self.load_user_page(username, user_role)


    def remember_checked(self):

        #Access the remember_var passed from the LoginPage instance
        #Checks if the remember_var attribute exists and if it is checked (True).
        if hasattr(self,'remember_var') and self.remember_var.get():
            return True
        return False

    #This method creates an instance of the LoginPage and sets its master to the background frame.
    def load_login_page(self):

        #Checks if self.current_page attribute is not None, and if so, it destroys the current page.
        if self.current_page:
            self.current_page.destroy()

        #Creates an instance of the LoginPage class and sets its master to the background frame.
        #Pass the app instance to the LoginPage so that it can access remember_var    
        self.login_page = LoginPage(master=self.background_frame, app=self)

        #After creating the new instance of LoginPage, this updates the self.current_page
        #attribute to hold a reference to the newly created LoginPage instance.
        self.current_page = self.login_page

        self.login_page.app = self


    def load_user_page(self, username, user_role):

        if self.current_page:
            self.current_page.destroy()

            #This method creates an instance of the MainPage class and sets its master to the background frame.
            #It also passes the username from LoginPage to the MainPage instance.
        self.user_page = UserMainPage(
            master=self.background_frame,
            username=username, 
            user_role=user_role, 
            app=self)
        
        self.user_page.app = self
        self.current_page = self.user_page
    

    def load_admin_page(self, username, user_role):

        if self.current_page:
            self.current_page.destroy()
        
        self.admin_page = AdminMainPage(master=self.background_frame, username=username, user_role=user_role)
        self.current_page = self.admin_page

        self.admin_page.app = self
       

    def load_signup_page(self):

        if self.current_page:
            self.current_page.destroy()
        
        self.signup_page = SignupPage(master=self.background_frame, app=self)
        self.current_page = self.signup_page

        self.signup_page.app = self

    
    def load_recover_password_page(self):
        
        if self.current_page:
            self.current_page.destroy()
        

    
    def on_close(self):

        print(f"DEBUG: Logging out user {self.logged_in_username}")
        
        auth = Authenticator()
        if self.logged_in_username:
            auth.logout_user(self.logged_in_username)
        if os.path.exists("session.json"):
            os.remove("session.json")
        self.destroy()


    def run(self):
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)  #Set close handler
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()