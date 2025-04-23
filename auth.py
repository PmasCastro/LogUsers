#takes care of user authentication, login, logouts

import sqlite3

DB_NAME = "users.db"

def log_in(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT isOnline FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    if result is None:
        print(f"User '{username}' does not exist.")
        conn.close()
        return
    if result[0] == 1:
        print(f"User '{username}' is already logged in")
        conn.close()
        return
    else:
        cursor.execute(
        "UPDATE users SET isOnline=1 WHERE username =?", (username,)
        
    )
    conn.commit()
    print(f"User '{username}' is logged in")
    conn.close()

    
def log_out(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET isOnline=0 WHERE username =?", (username,)
    )
    conn.commit()
    print(f"User '{username}' is logged out")
    conn.close()


log_out("Admin")