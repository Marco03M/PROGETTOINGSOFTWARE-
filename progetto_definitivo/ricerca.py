import random
import tkinter as tk
from tkinter import messagebox
import datetime


class Ricerca:




    def __init__(self, nome="Ricerca", dipendenti_Ricerca=50):
        self.nome = nome
        self.dipendenti_Ricerca = dipendenti_Ricerca


        try:
            with open('Anteriore.txt', 'r') as file:
                for linea in file:
                    chiave, valore = linea.strip().split(':')
                    valore = int(valore)
                    print(f"{chiave}: {valore}")

                    if chiave == 'budgetrimanente':
                        self.budget_Ricerca = valore



        except FileNotFoundError:
            print(f"Errore: il file  non è stato trovato.")

        self.budget_Ricerca




    def Ricerca_Materiale(self):
        numero_successo = random.randint(1, 4)
        self.costo_ricerca = random.randint(1000, 5000)
        self.budget_rimanente = self.budget_Ricerca - self.costo_ricerca

        if numero_successo == 1 and self.budget_rimanente > 0:
            result = f"È stato trovato un nuovo materiale, costato {self.costo_ricerca}, budget rimasto{self.budget_rimanente}\n"

            now = datetime.datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("storico.txt", "a") as file:
                    file.write(f"data nuovo materiale cercato:{formatted_date_time}\n")
                    file.write("lo sviluppo ha avuto successo\n")
                    file.write(f"costoanteriore:{self.costo_ricerca}\n")
                    file.write(f"budget rimanente ali anteriori:{self.budget_rimanente}\n\n\n")


            except Exception:
                print("errore")


        elif numero_successo > 1 and self.budget_rimanente > 0:
            result = f"Non è stato trovato nessun materiale, la ricerca è costata {self.costo_ricerca}, sono rimasti {self.budget_rimanente}"

            now = datetime.datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("storico.txt", "a") as file:
                    file.write(f"data nuovo materiale cercato:{formatted_date_time}\n")
                    file.write("lo sviluppo non ha avuto successo\n")
                    file.write(f"budget terminaato\n\n\n")


            except Exception:
                print("errore")

        elif self.budget_rimanente <= 0:
            result = "Il budget rimanente non è sufficiente per un nuovo materiale"
            now = datetime.datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("storico.txt", "a") as file:
                    file.write(f"data ala anteriore prodotta:{formatted_date_time}\n")
                    file.write("lo sviluppo non ha avuto successo\n")
                    file.write(f"costoanteriore:{self.costo_ricerca}\n")
                    file.write(f"budget rimanente ali anteriori:{self.budget_rimanente}\n\n\n")


            except Exception:
                print("errore")

        self.budget_Ricerca = self.budget_rimanente  # Aggiorna il budget rimanente
        return result


# Funzione per avviare la ricerca e mostrare il risultato
def avvia_ricerca():
    risultato = reparto_ricerca.Ricerca_Materiale()
    messagebox.showinfo("Risultato della Ricerca", risultato)


# Creazione della finestra principale
root = tk.Tk()
root.title("Sistema di Ricerca")
root.geometry("250x250")


# Creazione di un'istanza della classe Ricerca
reparto_ricerca = Ricerca()

# Creazione del pulsante per avviare la ricerca
btn_ricerca = tk.Button(root, text="Avvia Ricerca", command=avvia_ricerca)
btn_ricerca.pack(pady=20)

# Avvio del loop principale della GUI
root.mainloop()


