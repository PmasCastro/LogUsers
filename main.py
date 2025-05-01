from gui.login_page import LoginPage  # Import your GUI class
  # Import Authenticator

def run():
    login_app = LoginPage()
    login_app.mainloop() 

if __name__ == "__main__":
    run()  # Run the application when executing main.py