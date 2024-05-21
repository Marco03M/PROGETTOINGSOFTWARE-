import tkinter as tk
from Reparto import Anteriore


class post_race:


   def __init__(self, anteriore, log_text):
       self.reparto = anteriore
       self.log_text = log_text


   def gestisci_post_gara(self, statoTelaioPosteriore, statoMotore, aliDisp):
       self.log_text.insert(tk.END, "\n--- Gestione post-gara ---\n")


       # Esempio di chiamata ai metodi della classe Reparto
       if aliDisp < 4:
           risultato = self.anteriore.produci_anteriore()
           self.log_text.insert(tk.END, risultato + "\n")


       if statoMotore < 50:
           risultato = self.reparto.produci_motore()
           self.log_text.insert(tk.END, risultato + "\n")


       # Sostituzione dei componenti danneggiati
       if aliDisp < 4:
           risultato = self.reparto.sostituisci_ala()
           self.log_text.insert(tk.END, risultato + "\n")


       if statoMotore < 50:
           risultato = self.reparto.sostituisci_motore()
           self.log_text.insert(tk.END, risultato + "\n")


       self.log_text.insert(tk.END, "\n--- Fine gestione post-gara ---\n")
