import app
import controller

def start_app():
    app()  # Call the function to create the user interface
    controller()  # Call the function that handles GUI/DB interactions

if __name__ == "__main__":
    start_app()