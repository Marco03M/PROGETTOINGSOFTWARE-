import tkinter as tk
from tkinter import messagebox
def postrace(self):
    try:
        with open("stato_macchina.txt", "r") as file:
            contenuto = file.read()
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "\n--- Stato della Macchina ---\n")
            self.log_text.insert(tk.END, contenuto + "\n")
    except FileNotFoundError:
        messagebox.showerror("Errore", "Il file stato_macchina.txt non esiste.")

