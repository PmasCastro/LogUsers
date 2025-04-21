import ttkbootstrap as tb
from ttkbootstrap.constants import *

app = tb.Window(themename="darkly")   # Choose a theme
app.title("Login App")
app.geometry("300x200")

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


app.mainloop()