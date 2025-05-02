# This is the main entry point for the application. It initializes the GUI and starts the main loop.
# It also handles the flow of the app, including managing the flow between different pages.
from gui.login_page import LoginPage
from gui.main_page import MainPage
import customtkinter as ctk

class App(ctk.CTk):

    #Sets up the different pages' geometry
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Login App")

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
    
    #This method creates an instance of the LoginPage and sets its master to the background frame.
    def load_login_page(self):

        #Checks if self.current_page attribute is not None, and if so, it destroys the current page.
        if self.current_page:
            self.current_page.destroy()

        #Creates an instance of the LoginPage class and sets its master to the background frame.    
        self.login_page = LoginPage(master=self.background_frame)

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

    # This method is called when the app is closed and ensures proper cleanup.
    def run(self):
        
        """Run the main Tkinter loop."""
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
    
    

