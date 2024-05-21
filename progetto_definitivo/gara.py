import tkinter as tk
from tkinter import scrolledtext, messagebox

from Reparto import Reparto
from Reparto import Anteriore
from postgara import postrace

import random
import time


class GaraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stato della Gara")
        self.log_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Inizializza i valori della macchina solo una volta
        self.aliDisp = 4
        self.statoTelaioPosteriore = 100
        self.statoMGUH = 150
        self.statoMHUK = 150


        self.visualizza_file_btn = tk.Button(master, text="Visualizza stato macchina", command=self.post)
        self.visualizza_file_btn.pack(side=tk.BOTTOM, fill=tk.X)

        self.simula_successiva_btn = tk.Button(master, text="Simula successiva", command=self.simula_successiva)
        self.simula_successiva_btn.pack(side=tk.BOTTOM, fill=tk.X)

        self.accedi_btn = tk.Button(master, text="Accedi reparti", command=self.accedi_reparti)
        self.accedi_btn.pack(side=tk.BOTTOM, fill=tk.X)

        self.reparto = Reparto()


        self.gara_durata()

    def gara_durata(self):
        for secondo in range(1, 10):
            numeroTelaioAnteriore = random.randint(1, 100)
            numeroTelaioPosteriore = random.randint(1, 200)
            numeroMGUH = random.randint(1, 5)
            numeroMGUK =random.randint(1,5)

            if numeroTelaioAnteriore <= 10:
                self.log_text.insert(tk.END, "Il pilota sostituisce l'ala anteriore\n")
                self.aliDisp -= 1
                self.log_text.insert(tk.END, f"Il numero di ali nuove rimaste è {self.aliDisp}\n\n")

            if self.aliDisp == 0:
                self.log_text.insert(tk.END, "Hai finito i ricambi!! Gara terminata\n\n")
                self.salva_stato_macchina()
                return

            if numeroTelaioPosteriore <= 1:
                self.log_text.insert(tk.END, "Gara finita! Telaio posteriore rotto\n\n")
                self.statoTelaioPosteriore = 0
                self.salva_stato_macchina()
                return

            elif 5 < numeroTelaioPosteriore <= 15:
                self.statoTelaioPosteriore -= 5
                self.log_text.insert(tk.END, f"Il telaio posteriore è al {self.statoTelaioPosteriore}\n\n")

            if self.statoTelaioPosteriore == 0:
                self.log_text.insert(tk.END, "Il telaio è rotto! Gara finita\n\n")
                self.salva_stato_macchina()
                return

            self.statoMGUH -= numeroMGUH
            self.statoMHUK -= numeroMGUK

            if self.statoMHUK <= 5:
                self.log_text.insert(tk.END, "MGUK rotto, gara finita\n\n")
                self.statoMGUK = 0
                self.salva_stato_macchina()
                return

            else:
                self.log_text.insert(tk.END, f"l'MGUK è al {self.statoMHUK}%\n")



            if self.statoMGUH <= 5:
                self.log_text.insert(tk.END, "MGUH rotto, gara finita\n\n")
                self.statoMGUH = 0
                self.salva_stato_macchina()
                return

            else:
                self.log_text.insert(tk.END, f"l'MGUH è al {self.statoMGUH}%\n")

            self.log_text.insert(tk.END, f"Il telaio posteriore è al {self.statoTelaioPosteriore}%")
            self.log_text.insert(tk.END, f"\nIl numero di ali rimanenti è {self.aliDisp}\n\n")
            self.log_text.insert(tk.END, f"La gara è al {secondo}%\n")
            self.log_text.update()
            time.sleep(1)
            self.log_text.delete(1.0, tk.END)

        self.log_text.insert(tk.END, "La gara è stata completata senza problemi.\n\n")
        self.log_text.insert(tk.END, f"Stato telaio posteriore: {self.statoTelaioPosteriore}\n")
        self.log_text.insert(tk.END, f"Stato MGUH: {self.statoMGUH}\n")
        self.log_text.insert(tk.END, f"Stato MGUK: {self.statoMGUH}\n")
        self.salva_stato_macchina()


    def simula_successiva(self):
        self.log_text.delete(1.0, tk.END)
        self.gara_durata()  # Avvia una nuova simulazione

    def accedi_reparti(self):
        login_window = tk.Toplevel(self.master)
        login_window.title("Accesso ai Reparti")
        login_window.geometry("400x250")

        tk.Label(login_window, text="Nome utente:").pack(pady=5)
        self.username_entry = tk.Entry(login_window)
        self.username_entry.pack(pady=5)

        tk.Label(login_window, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(login_window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(login_window, text="Accedi", command=self.verifica_accesso).pack(pady=10)

    def verifica_accesso(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Esempio di verifica delle credenziali (da personalizzare)

        if username == "anteriore" and password == "anteriore":

            Anteriore.create_Anteriore(self)
            aliDisp += aliDisp





        elif username == "posteriore" and password == "posteriore":
         print ("dd")


        else:
            messagebox.showerror("Errore", "Nome utente o password non corretti")

    def salva_stato_macchina(self):
        try:
            with open("stato_macchina.txt", "w") as file:
                file.write(f"Stato telaio posteriore: {self.statoTelaioPosteriore}%\n")
                file.write(f"Stato MGUK: {self.statoMHUK}\n")
                file.write(f"Stato MGUH: {self.statoMGUH}%\n")
                file.write(f"Numero di ali rimanenti: {self.aliDisp}\n")
            self.log_text.insert(tk.END, "Stato della macchina salvato su stato_macchina.txt\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"Errore durante il salvataggio del file: {e}\n")


    def post(self):
        postrace(self)



root = tk.Tk()
app = GaraGUI(root)
root.mainloop()

