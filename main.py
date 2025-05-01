from gui.login_page import LoginPage
import customtkinter as ctk 
import tkinter.messagebox as tkmb  


class AppController:
    def __init__(self):
        self.root = ctk.CTk()  # Create the main application window
        self.root.geometry("350x400")  # Set the window size
        self.root.title("Login App")  # Set the window title

        # Configure grid layout for the main window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create an instance of the LoginPage class
        self.login_page = LoginPage(master=self.root)
    
    


    def run(self):
        self.login_page.pack(expand=True, fill="both")  # Pack the login page into the main window
        self.root.mainloop()  # Start the main event loop




def run():
    login_app = LoginPage()
    
    # Bind the close event to a custom function
    login_app.protocol("WM_DELETE_WINDOW", login_app.on_close)
    
    login_app.mainloop()  # Run the application

if __name__ == "__main__":
    run()  # Run the application when executing main.py