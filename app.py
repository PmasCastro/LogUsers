#User interface outline
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from controller import create_new_user

app = tb.Window(themename="darkly")   # Choose a theme
app.title("Login App")
app.geometry("1200x900")

#Username
username_label = tb.Label(app, text="Username:")
username_label.pack(side="left", padx=5, pady=5)
username_entry = tb.Entry(app)
username_entry.pack(side="left", padx=5, pady=5)

#Password
password_label = tb.Label(app, text="Password:")
password_label.pack(side="left", padx=5, pady=5)
password_entry = tb.Entry(app, show="*")
password_entry.pack(side="left", padx=5, pady=5)

#Create user button

create_user_button = tb.Button(
    app,
    text="Create",
    command=lambda: create_new_user(username_entry, password_entry)
)
create_user_button.pack(side="left", padx=5, pady=5)


app.mainloop()