from pannello import *
from impianto import *

def main():
    pannello1 = PannelloFotovoltaico("01", "prova1", 12.0)
    pannello2 = PannelloFotovoltaico("02", "prova2", 20.0)
    
    impianto = ImpiantoSolare("01", "prova1", "cesena" 100, "attivo")
    impianto.aggiungi_pannello(pannello1)
    
if __name__ == "__main__":
    main()