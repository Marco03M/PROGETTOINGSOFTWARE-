import tkinter as tk
from tkinter import messagebox

try:
    with open('MGUH.txt', 'w') as file:
        file.write(f"budgetrimanente:500000\n")
except FileNotFoundError:
    print(f"Errore: il file  non è stato trovato.")

try:
    with open('MGUK.txt', 'w') as file:
        file.write(f"budgetrimanente:500000\n")
except FileNotFoundError:
    print(f"Errore: il file  non è stato trovato.")

try:
    with open('telaio_post.txt', 'w') as file:
        file.write(f"budgetrimanente:500000")
except FileNotFoundError:
    print(f"Errore: il file  non è stato trovato.")

try:
    with open('Anteriore.txt', 'w') as file:
        file.write(f"budgetrimanente:500000\n")
        file.write("aliDisp:0\n")
except FileNotFoundError:
    print(f"Errore il non è stato trovato")

Areodinamica_completata = False
Powerunit_completata = False

def login():
    global Areodinamica_completata
    global Powerunit_completata

    username= username_entry.get()
    password = password_entry.get()

    if username == "gara" and password == "gara":
        if Areodinamica_completata == True and Powerunit_completata == True:
            import gara
            gara
        else:
            messagebox.showerror("errore","Non hai completato la macchina, completala e riprova")



    if username == "powerunit" and password == "powerunit":
        Powerunit_completata = True
        import powerunit
        powerunit.pw()

    if username == "areodinamica" and password == "areodinamica":
        Areodinamica_completata = True
        import Areodinamica
        Areodinamica.areo()



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
