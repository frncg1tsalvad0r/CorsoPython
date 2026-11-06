class Biglietto:
    id_biglietto = 0
    nome_passeggero = ""
    partenza = ""
    data_partenza = ""
    destinazione = ""
    codice_volo = 0

    def __init__(self, idb, np, pa, dp, de, cv):
        self.id_biglietto = idb
        self.nome_passeggero = np
        self.partenza = pa
        self.data_partenza = dp
        self.destinazione = de
        self.codice_volo = cv
        

    def __str__(self):
        return str(self.id_biglietto) + "," + self.nome_passeggero
        
    
    def funzione(self):
        '''
        modifico o uso i bilietto
        '''
        print(self.id_passeggero)

class Compagnia:
    biglietti  = []

    def __str__(self):
        s = ""
        for i in range(len(self.biglietti)):
           s+= str(self.biglietti[i]) + "\n"
        return s
    
    def inserisci_biglietto(self, b):
        self.biglietti.append(b)

    def rimuovi_biglietto_da_id(self, id):
        for i in range(len(self.biglietti)):
           if self.biglietti[i].id_biglietto == id:
               del self.biglietti[i]
               return
        return

    def rimuovi_biglietto_da_nome(self, nome):
        for i in range(len(self.biglietti)):
           if self.biglietti[i].nome_passeggero == nome:
               del self.biglietti[i]
               return
        return

    def conta_bilietti(self, nome):
        conta= 0
        for i in range(len(self.biglietti)):
           if self.biglietti[i].nome_passeggero == nome:
               conta += 1
               
        return conta

c = Compagnia()           
b1 = Biglietto(1000, "Mario", "Milano", "2026-01-01", "Roma", 208)
b2 = Biglietto(1001, "Mario", "Milano", "2026-01-01", "Roma", 208)
c.inserisci_biglietto(b1)
c.inserisci_biglietto(b2)
print(str(c))
nb = c.conta_bilietti("Mario")
print(f"Biglietti {nb}")
c.rimuovi_biglietto_da_id(1000)
c.rimuovi_biglietto_da_nome("Mario")


