class PannelloFotovoltaico:
    def __init__(self, codice: str, modello: str, potenza_kw: float) -> None:
        if (codice is None): raise ValueError("Codice non può essere null") 
        self.codice = codice
        if (modello is None): raise ValueError("Modello non può essere null") 
        self.modello = modello
        if (potenza_kw is None): raise ValueError("Potenza non può essere null")
        if (potenza_kw<0.0): raise ValueError("Potenza non può negativa") 
        self.potenza_kw = potenza_kw
        
            
    