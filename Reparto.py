import random

class Reparto:
    def __init__(self, dipendenti_totali=1000, budget_totale=150000000):
        self.dipendenti_totali = dipendenti_totali
        self.budget_totale = budget_totale


class Aerodinamica(Reparto):
    def __init__(self, nome="Aerodinamica", dipendenti_Anteriore=50, dipendenti_Posteriore=50, budget_AD=1000000):
        super().__init__()
        self.nome = nome
        self.dipendenti_Anteriore = dipendenti_Anteriore
        self.dipendenti_Posteriore = dipendenti_Posteriore
        self.budget_AD = budget_AD


budget_Anteriore=5000000
class Anteriore(Aerodinamica):
    def __init__(self, statoDiSviluppo, condizione, aliDisp, dipendenti_Anteriore=50 ):
        super().__init__(dipendenti_Anteriore)
        self.statoDiSviluppo = statoDiSviluppo
        self.condizione = condizione
        self.aliDisp = aliDisp
        self.budget_Anteriore = budget_Anteriore

    def create_Anteriore(self):
        global budget_Anteriore
        costo = random.randint(150000, 200000)
        if costo <= budget_Anteriore:
            budget_Anteriore -= costo
            print("Costo Ala Anteriore:", costo)
            print("Puoi procedere alla realizzazione dell'ala anteriore")
            print("Budget Anteriore Rimanente:", budget_Anteriore)
        else:
            print("Siamo a corto di fondi non possiamo costruire questa ala anteriore")

budget_Posteriore=5000000
class Posteriore(Aerodinamica):
    def __init__(self, statoDiSviluppo, condizione, aliDisp, dipendenti_Posteriore=50 ):
        super().__init__(dipendenti_Posteriore)
        self.statoDiSviluppo = statoDiSviluppo
        self.condizione = condizione
        self.aliDisp = aliDisp
        self.budget_Posteriore = budget_Posteriore

    def create_posteriore(self):
        global budget_Posteriore
        costo=random.randint(150000,200000)
        if costo <= budget_Posteriore:
            budget_Posteriore -= costo
            print("Costo Telaio Posteriore:", costo)
            print("Puoi procedere alla realizzazione del telaio posteriore")
            print("Budget Posteriore Rimanente:", budget_Posteriore)
        else:
            print("Siamo a corto di fondi non possiamo costruire questo telaio posteriore")

class PowerUnit(Reparto):
    def __init__(self, nome="Power Unit", dipendenti_MGUH=50, dipendenti_MGUK=50, budget_PO=100000000):
        super().__init__()
        self.nome = nome
        self.dipendenti_MGUH = dipendenti_MGUH
        self.dipendenti_MGUK = dipendenti_MGUK
        self.budget_PO = budget_PO

budget_MGUK = 10000000

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

budget_MGUH = 10000000

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

class Ricera(Reparto):
    def __init__(self,nome="Ricerca", dipendenti_Ricerca=50):
        super().__init__()
        self.nome=nome
        self.dipendenti_Ricerca=dipendenti_Ricerca

    budget_Ricerca=1000000
    def Ricerca_Materiale(self):
        global budget_Ricerca
