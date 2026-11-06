class Prenotazione:
    id_prenotazione = 0
    nome_cliente = ""
    nome_film = ""
    data_ora = ""
    posizione = ""


    def __init__(self, idp, nc, nf, do, po):
        self.id_prenotazione = idp
        self.nome_cliente = nc
        self.nome_film = nf
        self.data_ora = do
        self.posizione = po

    def __str__(self):
        return str(self.id_prenotazione) + self.nome_cliente 
    
    def metodo(self):
        print(self.nome_cliente)

class Cinema:
    prenotazioni = []

    def inserisci_prenotazione(self, pr):
        self.prenotazioni.append(pr)

    def rimuovi_prenotazione_da_id(self, id):
        for i in range(len(self.prenotazioni)):
            if self.prenotazioni[i].id_prenotazione == id:
                del self.prenotazioni[i]
                return
        return
    def rimuovi_prenotazione_da_cliente(self, nc):
        for i in range(len(self.prenotazioni)):
            if self.prenotazioni[i].nome_cliente == nc:
                del self.prenotazioni[i]
                return
        return

    def __str__(self):
        s = "Cinema\n"
        for i in range(len(self.prenotazioni)):
            s += str(self.prenotazioni[i]) + "\n"

        return s
    
    def conta_biglietti_da_cliente(self, nc):
        conta = 0
        for i in range(len(self.prenotazioni)):
            if self.prenotazioni[i].nome_cliente == nc:
                conta+=1
        return conta
    
c = Cinema()

p = Prenotazione(1000, "Mirco Rossi", "Titanic", "2026-02-02 15:30", "A 8")
p.metodo()
print(p)
p1 = Prenotazione(1001, "Mirco Rossi", "Titanic", "2026-02-03 15:30", "A 8")
print(p1)
#metodo(p)
c.inserisci_prenotazione(p)
c.inserisci_prenotazione(p1)

print(c)

conteggio =  c.conta_biglietti_da_cliente("Mirco Rossi")
print(conteggio)
