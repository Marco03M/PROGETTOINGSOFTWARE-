import datetime
import random
from Reparto import Aerodinamica
import tkinter as tk
from tkinter import messagebox
class Anteriore(Aerodinamica):
        def __init__(self,budget_Anteriore, dipendenti_Anteriore=50, ):
            super().__init__(dipendenti_Anteriore=dipendenti_Anteriore)
            self.budget_Anteriore = budget_Anteriore

        def create_anteriore(self, costo):
            if costo <= self.budget_Anteriore:
                self.budget_Anteriore -= costo
                return True, self.budget_Anteriore
            else:
                return False, self.budget_Anteriore
class Posteriore(Aerodinamica):
        def __init__(self, budget_Posteriore, dipendenti_Posteriore=50, ):
            super().__init__(dipendenti_Posteriore=dipendenti_Posteriore)
            self.budget_Posteriore = budget_Posteriore

        def create_posteriore(self, costo):
            if costo <= self.budget_Posteriore:
                self.budget_Posteriore -= costo
                return True, self.budget_Posteriore
            else:
                return False, self.budget_Posteriore

class AreodinamicaGUI:
        def __init__(self, master):

            try:
                with open('Anteriore.txt', 'r') as file:
                    for linea in file:
                        chiave, valore = linea.strip().split(':')
                        valore = int(valore)
                        print(f"{chiave}: {valore}")


                        if chiave == 'budgetrimanente':
                            self.budgetanteriore = valore

                        if chiave == 'aliDisp':
                            self.ali = valore

            except FileNotFoundError:
                print(f"Errore: il file  non è stato trovato.")



            try:
                with open('telaio_post.txt', 'r') as file:
                    for linea in file:
                        chiave, valore = linea.strip().split(':')
                        valore = int(valore)
                        print(f"{chiave}: {valore}")

                        if chiave == 'budgetrimanente':
                            self.budgetposteriore = valore

            except FileNotFoundError:
                print(f"Errore: il file  non è stato trovato.")


            self.master = master
            self.master.title("Gestione PowerUnit")
            self.areodinamica=Aerodinamica()
            self.anteriore=Anteriore(budget_Anteriore=self.budgetanteriore)
            self.posteriore=Posteriore(budget_Posteriore=self.budgetposteriore)

            self.setup_gui()

        def setup_gui(self):
            tk.Label(self.master, text="Dipendenti Anteriore:").grid(row=0, column=0, padx=10, pady=5)
            self.dipendenti_anteriore_label = tk.Label(self.master, text=self.anteriore.dipendenti_Anteriore)
            self.dipendenti_anteriore_label.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(self.master, text="Dipendenti Posteriore:").grid(row=1, column=0, padx=10, pady=5)
            self.dipendenti_posteriore_label = tk.Label(self.master, text=self.posteriore.dipendenti_Posteriore)
            self.dipendenti_posteriore_label.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(self.master, text="Budget Anteriore:").grid(row=2, column=0, padx=10, pady=5)
            self.budget_anteriore_label = tk.Label(self.master, text=f"${self.anteriore.budget_Anteriore}")
            self.budget_anteriore_label.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(self.master, text="Budget Posteriore:").grid(row=3, column=0, padx=10, pady=5)
            self.budget_posteriore_label = tk.Label(self.master, text=f"${self.posteriore.budget_Posteriore}")
            self.budget_posteriore_label.grid(row=3, column=1, padx=10, pady=5)

            self.mguk_button = tk.Button(self.master, text="Crea anteriore", command=self.create_anteriore)
            self.mguk_button.grid(row=4, column=0, padx=10, pady=10)

            self.mguh_button = tk.Button(self.master, text="Crea posteriore", command=self.create_posteriore)
            self.mguh_button.grid(row=4, column=1, padx=10, pady=10)

        def create_anteriore(self):

            costo = random.randint(15000, 20000)
            success, budget_rimanente = self.anteriore.create_anteriore(costo)
            if success:
                self.ali = self.ali +1
                print(self.ali)
                messagebox.showinfo("Successo", f"Ala anteriore creata con successo! Costo: ${costo}")



                try:
                    with open("Anteriore.txt", "w") as file:
                            file.write(f"costoanteriore:{costo}\n")
                            file.write(f"budgetrimanente:{budget_rimanente}\n")
                            file.write(f"aliDisp:{self.ali}\n")

                except Exception as e:
                    self.log_text.insert(tk.END, f"Errore durante il salvataggio del file: {e}\n")

                try:
                        with open("storico.txt", "a) as file:
                        file.write(f"data ala anteriore prodotta:{formatted_date_time}\n")
                        file.write(f"costoanteriore:{costo}\n")
                        file.write(f"budget rimanente ali anteriori:{budget_rimanente}\n")
                        file.write(f"numero ali rimanenti:{self.aliDisp}\n\n\n")


                except Exception as e:
                    self.log_text.insert(tk.END, f"Errore durante il salvataggio del file: {e}\n")
                
            else:
                messagebox.showerror("Errore", f"Fondi insufficienti per creare l'ala anteriore. Costo: ${costo}")
            self.update_budget_anteriore_label(budget_rimanente)

        def create_posteriore(self):
            costo = random.randint(150000, 200000)
            success, budget_rimanente = self.posteriore.create_posteriore(costo)
            if success:
                messagebox.showinfo("Successo", f"posteriore è creato con successo! Costo: ${costo}")

                try:
                    with open("telaio_post.txt", "w") as file:
                        file.write(f"costoposteriore:{costo}\n")
                        file.write(f"Stato telaio posteriore:100\n")
                        file.write(f"budgetrimanente:{budget_rimanente}\n")

                except Exception as e:
                    self.log_text.insert(tk.END, f"Errore durante il salvataggio del file: {e}\n")

                try:
                    with open("storico.txt", "a") as file:
                        file.write(f"data telaio posteriore prodotto:{formatted_date_time}\n")
                        file.write(f"costoposteriore:{costo}\n")
                        file.write(f"Stato telaio posteriore 100\n")
                        file.write(f"budget rimanente telaio posteriore:{budget_rimanente}\n\n\n")


                except Exception as e:
                    self.log_text.insert(tk.END, f"Errore durante il salvataggio del file: {e}\n")
                
            else:
                messagebox.showerror("Errore", f"Fondi insufficienti per creare il telaio posteriore. Costo: ${costo}")
            self.update_budget_posteriore_label(budget_rimanente)

        def update_budget_anteriore_label(self, budget_rimanente):
            self.budget_anteriore_label.config(text=f"${budget_rimanente}")

        def update_budget_posteriore_label(self, budget_rimanente):
            self.budget_posteriore_label.config(text=f"${budget_rimanente}")


def accedi_aerodinamica():
    root = tk.Tk()
    app = AreodinamicaGUI(master=root)
    root.mainloop()
if __name__ == "__main__":
    accedi_aerodinamica()
