from pannello import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        if (codice is None): raise ValueError("Codice non può essere null") 
        self.codice = codice
        
        if (modello is None): raise ValueError("Modello non può essere null") 
        self.modello = modello
        
        if (localita is None): raise ValueError("Localita non può essere null") 
        self.localita = localita
        
        if (potenza_massima_kw is None): raise ValueError("Potenza massima non può essere null")
        if (potenza_massima_kw<0.0): raise ValueError("Potenza massima non può negativa") 
        self.potenza_massima_kw = potenza_massima_kw
        
        if (stato is None): raise ValueError("Stato non può essere null") 
        self.stato = stato
        
        self.pannelli = []
        
        
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
        if (pannello is None): raise ValueError("Pannello non può essere null")
        for p in self.panelli:
            if (p.codice == panello.codice): raise ValueError("Codice già presente")
            
        if (potenza_pannelli() + pannello.potenza_kw > potenza_massima_kw): raise ValueError("Potenza max superata")       
        self.pannelli.append(pannello)

        
        
    def potenza_pannelli(self) -> float:
        potenza_tot = 0.0
        for p in self.panelli:
            potenza_tot += p.potenza_kw
            
        return potenza_tot           
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        for p in self.panelli:
            if (p.codice == codice): return p
        return None
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        pannello = cerca_pannello(codice) 
        if(pannello is None):
            return None
        else:
            self.pannelli.remove(pannello)
            return pannello
    
    def pannelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]:
        result = [p for p in self.panelli if p.potenza_kw <= potenza_massima ]
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    