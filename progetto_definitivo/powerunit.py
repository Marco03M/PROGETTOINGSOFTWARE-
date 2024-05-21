import random
from Reparto import PowerUnit
budget_MGUK=10000000
class MGUK(PowerUnit):
    def __init__(self, statoDiSviluppo, condizione, dipendenti_MGUK=50):
            super().__init__(dipendenti_MGUK)
            self.statoDiSviluppo = statoDiSviluppo
            self.condizione = condizione
            self.budget_MGUK = budget_MGUK


    def create_MGUK(self):
        global budget_MGUK
        costo = random.randint(150000, 200000)
        if costo <= budget_MGUK:
             budget_MGUK -= costo
             print("Costo MGUK:", costo)
             print("Puoi procedere alla realizzazione del MGUK")
             print("Budget MGUK Rimanente:", budget_MGUK)
        else:
            print("Siamo a corto di fondi non possiamo costruire MGUK")

budget_MGUH=10000000
class MGUH(PowerUnit):
    def __init__(self, statoDiSviluppo, condizione, dipendenti_MGUH=50):
            super().__init__(dipendenti_MGUH)
            self.statoDiSviluppo = statoDiSviluppo
            self.condizione = condizione
            self.budget_MGUH = budget_MGUH


    def create_MGUH(self):
        global budget_MGUH
        costo = random.randint(150000, 200000)
        if costo <= budget_MGUH:
             budget_MGUH -= costo
             print("Costo MGUK:", costo)
             print("Puoi procedere alla realizzazione del MGUH")
             print("Budget MGUH Rimanente:", budget_MGUH)
        else:
            print("Siamo a corto di fondi non possiamo costruire MGUH")

mguh1=MGUH("in preparazione", "buone",50 )
print(mguh1.create_MGUH())
mguk2=MGUK("in preparazione", "buone",50)
print(mguk2.create_MGUK())