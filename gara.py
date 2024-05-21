import tkinter as tk
from tkinter import scrolledtext, messagebox

from postgara import post_race
from Reparto import Reparto

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
        self.statoMotore = 150

        self.visualizza_file_btn = tk.Button(master, text="Visualizza stato macchina", command=self.visualizza_file)
        self.visualizza_file_btn.pack(side=tk.BOTTOM, fill=tk.X)

        self.simula_successiva_btn = tk.Button(master, text="Simula successiva", command=self.simula_successiva)
        self.simula_successiva_btn.pack(side=tk.BOTTOM, fill=tk.X)

        self.reparto = Reparto()
        self.post_gara = post_race(self.reparto, self.log_text)

        self.gara_durata()

    def gara_durata(self):
        for secondo in range(1, 10):
            numeroTelaioAnteriore = random.randint(1, 100)
            numeroTelaioPosteriore = random.randint(1, 200)
            numeroMotore = random.randint(1, 5)

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

            self.statoMotore -= numeroMotore

            if self.statoMotore <= 5:
                self.log_text.insert(tk.END, "Motore rotto, gara finita\n\n")
                self.statoMotore = 0
                self.salva_stato_macchina()
                return

            else:
                self.log_text.insert(tk.END, f"Il motore è al {self.statoMotore}%\n")

            self.log_text.insert(tk.END, f"Il telaio posteriore è al {self.statoTelaioPosteriore}%")
            self.log_text.insert(tk.END, f"\nIl numero di ali rimanenti è {self.aliDisp}\n\n")
            self.log_text.insert(tk.END, f"La gara è al {secondo}%\n")
            self.log_text.update()
            time.sleep(1)
            self.log_text.delete(1.0, tk.END)

        self.log_text.insert(tk.END, "La gara è stata completata senza problemi.\n\n")
        self.log_text.insert(tk.END, f"Stato telaio posteriore: {self.statoTelaioPosteriore}\n")
        self.log_text.insert(tk.END, f"Stato motore: {self.statoMotore}\n")
        self.salva_stato_macchina()
        self.post_gara.gestisci_post_gara(self.statoTelaioPosteriore, self.statoMotore, self.aliDisp)

    def simula_successiva(self):
        self.log_text.delete(1.0, tk.END)  # Pulisce il log
        self.gara_durata()  # Avvia una nuova simulazione

    def salva_stato_macchina(self):
        try:
            with open("stato_macchina.txt", "w") as file:
                file.write(f"Stato telaio posteriore: {self.statoTelaioPosteriore}%\n")
                file.write(f"Stato motore: {self.statoMotore}%\n")
                file.write(f"Numero di ali rimanenti: {self.aliDisp}\n")
            self.log_text.insert(tk.END, "Stato della macchina salvato su stato_macchina.txt\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"Errore durante il salvataggio del file: {e}\n")

    def visualizza_file(self):
        try:
            with open("stato_macchina.txt", "r") as file:
                contenuto = file.read()
                self.log_text.insert(tk.END, "\n--- Stato della Macchina ---\n")
                self.log_text.insert(tk.END, contenuto + "\n")
        except FileNotFoundError:
            messagebox.showerror("Errore", "Il file stato_macchina.txt non esiste.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GaraGUI(root)
    root.mainloop()
