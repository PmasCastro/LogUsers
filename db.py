#This file only handles db interactions: connects the db on init; adds new users; checks if user exists etc

import sqlite3

DB_NAME = "users.db"

def init_db():
    #Connects to the db; creates table if doesn't exist
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor() #creates cursor to execute sql commands

    # Create the users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

#Add new user to db
def add_user(username, password):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        #VALUES (?, ?) prevents SQL injection
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print(f"User '{username}' added successfully.")

    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    # Uncomment the next line if you need to create admin user
    # add_user("admin", "admin123")

add_user("Pedro Castro", "12345")