import tkinter as tk
from tkinter import messagebox

class Team:
   global dipendenti_totale
   dipendenti_totale = 1000
   global budget_tot
   budget_tot = 150000000

gara_completata = False

def login():
        global gara_completata

        username = username_entry.get()
        password = password_entry.get()

        if username == "gara" and password == "gara":
                import gara
                gara.GaraGUI
                gara_completata = True
                print("ciao")

        elif username == "postgara" and password == "postgara":
            if gara_completata:
                import postgara
                postgara.post_race
            else:
                messagebox.showerror("Accesso negato", "Completa Gara prima di accedere a Post Gara.")

        elif username =="reparto" and password == "reparto":
            import Reparto
            Reparto.Reparto
            print("ciao reparto")
        else:
             messagebox.showerror("Accesso negato", "Credenziali non valide.")


# Creazione della finestra principale
root = tk.Tk()
root.title("Accesso")

# Elementi dell'interfaccia per il login
tk.Label(root, text="Nome utente:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry = tk.Entry(root)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Bottone per effettuare il login
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

# Esecuzione dell'interfaccia grafica
root.mainloop()