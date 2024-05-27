import tkinter as tk
from tkinter import messagebox

from gara import GaraGUI
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
        try:
            import gara
            GaraGUI.gara_durata(self)  # Assumi che GaraGUI sia una classe e la stai istanziando
            gara_completata = True
            print("ciao")
        except ImportError:
            messagebox.showerror("Errore", "Impossibile importare il modulo gara.")
        except AttributeError:
            messagebox.showerror("Errore", "Classe GaraGUI non trovata nel modulo gara.")

    elif username == "postgara" and password == "postgara":
        if gara_completata:
            try:
                import postgara
                postgara.post_race()  # Assumi che post_race sia una funzione
            except ImportError:
                messagebox.showerror("Errore", "Impossibile importare il modulo postgara.")
            except AttributeError:
                messagebox.showerror("Errore", "Funzione post_race non trovata nel modulo postgara.")
        else:
            messagebox.showerror("Accesso negato", "Completa Gara prima di accedere a Post Gara.")

    elif username == "reparto" and password == "reparto":
        try:
            import Reparto
            Reparto.Reparto()  # Assumi che Reparto sia una classe e la stai istanziando
            print("ciao reparto")
        except ImportError:
            messagebox.showerror("Errore", "Impossibile importare il modulo Reparto.")
        except AttributeError:
            messagebox.showerror("Errore", "Classe Reparto non trovata nel modulo Reparto.")
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
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Bottone per effettuare il login
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

# Esecuzione dell'interfaccia grafica
root.mainloop()
