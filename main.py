# This is the main entry point for the application. It initializes the GUI and starts the main loop.
# It also handles the flow of the app, including managing the flow between different pages.


#Data flow management: Now the App and LoginPage share the remember_var
#allowing the app to properly handle user session persistence
#(e.g., saving/loading the "Remember me" state in session.json).


from gui.login_page import LoginPage
from gui.main_page import MainPage
import customtkinter as ctk
from auth import Authenticator  

class App(ctk.CTk):

    #Sets up the different pages' geometry
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Login App")

        self.logged_in_username = None

        # Configure grid for the main window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Outer frame with background color
        self.background_frame = ctk.CTkFrame(self, fg_color="#4C5B61")
        self.background_frame.grid(row=0, column=0, sticky="nsew")
        self.background_frame.grid_rowconfigure(0, weight=1)
        self.background_frame.grid_columnconfigure(0, weight=1)
        
        #Keeps track of the current page
        self.current_page = None 
        
        #Loads the login page on app start
        self.load_login_page()
        
        self.login_page.app = self
    
    def remember_checked(self):

        #Access the remember_var passed from the LoginPage instance
        #Checks if the remember_var attribute exists and if it is checked (True).
        if hasattr(self,'rember_var') and self.remember_var.get():
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

    def load_main_page(self, username):
        if self.current_page:
            self.current_page.destroy()

            #This method creates an instance of the MainPage class and sets its master to the background frame.
            #It also passes the username from LoginPage to the MainPage instance.
        self.main_page = MainPage(master=self.background_frame, username=username)
        self.current_page = self.main_page

        self.main_page.app = self
        
    def load_signup_page(self):
        pass
    
    def load_forgot_password_page(self):
        pass



    def load_user_settings(self):
        pass


    def on_close(self):

        #Checks if the user is logged in and if the remember me checkbox is not checked.
        #It logs the user out
        if self.logged_in_username and not self.remember_checked():
            auth = Authenticator()
            auth.logout(self.logged_in_username)
        self.destroy()

    def run(self):
        self.protocol("WM_DELETE_WINDOW", self.on_close)  #Set close handler
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
    
    

