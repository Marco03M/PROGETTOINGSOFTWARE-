import tkinter as tk
from tkinter import messagebox



from Reparto import Reparto

def login():
    global gara_completata

    username= username_entry.get()
    password = password_entry.get()

    if username == "gara" and password == "gara":
        import gara
        gara.GaraGUI



root=tk.Tk()
root.title("login team")
root.geometry("250x200")

tk.Label(root, text="nome utente:").grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="password:").grid(row= 4, column=1, padx =10, pady=5)
username_entry=tk.Entry(root)
password_entry=tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)
password_entry.grid(row=5, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="accedi", command=login)
login_button.grid(row=7, column= 1, padx=10)

root.mainloop()
