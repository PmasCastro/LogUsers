from gui.login_page import LoginPage  # Import your GUI class

def run():
    login_app = LoginPage()
    
    # Bind the close event to a custom function
    login_app.protocol("WM_DELETE_WINDOW", login_app.on_close)
    
    login_app.mainloop()  # Run the application

if __name__ == "__main__":
    run()  # Run the application when executing main.py