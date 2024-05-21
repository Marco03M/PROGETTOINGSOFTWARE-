import tkinter as tk
from tkinter import messagebox
from Reparto import Aerodinamica
import random
class Anteriore(Aerodinamica):
    def __init__(self,budget_Anteriore, dipendenti_Anteriore=50):
        super().__init__(dipendenti_Anteriore=dipendenti_Anteriore)
        self.budget_Anteriore = budget_Anteriore

    def create_anteriore(self, costo):
        if costo <= self.budget_Anteriore:
            self.budget_Anteriore -= costo
            return True, self.budget_Anteriore
        else:
            return False, self.budget_Anteriore

class Posteriore(Aerodinamica):
    def __init__(self, budget_Posteriore, dipendenti_Posteriore=50 ):
        super().__init__(dipendenti_Posteriore=dipendenti_Posteriore)
        self.budget_Posteriore = budget_Posteriore

    def create_posteriore(self, costo):
        if costo <= self.budget_Posteriore:
            self.budget_Posteriore -= costo
            return True, self.budget_Posteriore
        else:
            return False, self.budget_Posteriore

class AerodinamicaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Aerodinamica")

        self.aerodinamica = Aerodinamica()
        self.anteriore=Anteriore(budget_Anteriore=5000000)
        self.posteriore=Posteriore(budget_Posteriore=5000000)

        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.master, text="Dipendenti Anteriore:").grid(row=0, column=0, padx=10, pady=5)
        self.dipendenti_anteriore_label = tk.Label(self.master, text=self.aerodinamica.dipendenti_Anteriore)
        self.dipendenti_anteriore_label.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Dipendenti Posteriore:").grid(row=1, column=0, padx=10, pady=5)
        self.dipendenti_posteriore_label = tk.Label(self.master, text=self.aerodinamica.dipendenti_Posteriore)
        self.dipendenti_posteriore_label.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Budget Anteriore:").grid(row=2, column=0, padx=10, pady=5)
        self.budget_anteriore_label = tk.Label(self.master, text=f"${self.aerodinamica.budget_Anteriore}")
        self.budget_anteriore_label.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Budget Posteriore:").grid(row=3, column=0, padx=10, pady=5)
        self.budget_posteriore_label = tk.Label(self.master, text=f"${self.aerodinamica.budget_Posteriore}")
        self.budget_posteriore_label.grid(row=3, column=1, padx=10, pady=5)

        self.anteriore_button = tk.Button(self.master, text="Crea Ala Anteriore", command=self.create_anteriore)
        self.anteriore_button.grid(row=4, column=0, padx=10, pady=10)

        self.posteriore_button = tk.Button(self.master, text="Crea Telaio Posteriore", command=self.create_posteriore)
        self.posteriore_button.grid(row=4, column=1, padx=10, pady=10)

    def create_anteriore(self):
        costo = random.randint(150000, 200000)
        success, budget_rimanente = self.anteriore.create_anteriore(costo)
        if success:
            messagebox.showinfo("Successo", f"Ala Anteriore creata con successo! Costo: ${costo}")
        else:
            messagebox.showerror("Errore", f"Fondi insufficienti per creare l'ala anteriore. Costo: ${costo}")
        self.update_budget_anteriore_label(budget_rimanente)

    def create_posteriore(self):
        costo = random.randint(150000, 200000)
        success, budget_rimanente = self.posteriore.create_posteriore(costo)
        if success:
            messagebox.showinfo("Successo", f"Telaio Posteriore creato con successo! Costo: ${costo}")
        else:
            messagebox.showerror("Errore", f"Fondi insufficienti per creare il telaio posteriore. Costo: ${costo}")
        self.update_budget_posteriore_label(budget_rimanente)

    def update_budget_anteriore_label(self, budget_rimanente):
        self.budget_anteriore_label.config(text=f"${budget_rimanente}")

    def update_budget_posteriore_label(self, budget_rimanente):
        self.budget_posteriore_label.config(text=f"${budget_rimanente}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AerodinamicaGUI(master=root)
    root.mainloop()
