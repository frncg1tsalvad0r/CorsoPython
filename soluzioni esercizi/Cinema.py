class Prenotazione:
    id = 0
    cliente = ""
    nome_film = ""
    data_ora = ""
    posizione = 0

    def __init__(self, id, cliente, nome_film, data_ora, posizione):
        self.id = id
        self.cliente = cliente
        self.nome_film = nome_film
        self.data_ora = data_ora
        self.posizione = posizione

        
    def __str__(self):
        return str(self.id) + self.cliente + self.nome_film + self.data_ora  + str(self.posizione)


class Cinema:
    prenotazioni = []

    def __init__(self):
        pass

    def __str__(self):
        s = ""
        for i in range(0, len(self.prenotazioni)):
            s += str(self.prenotazioni[i]) + "\n"

        return s
    
    def inserisci_prenotazione(self, prenotazione):
        self.prenotazioni.append(prenotazione)

    def rimuovi_da_id(self, id):
        for i in range(0, len(self.prenotazioni)):
            if self.prenotazioni[i].id == id:
                del self.prenotazioni[i]
                break;

    def rimuovi_da_cliente(self, cliente):
        for i in range(0, len(self.prenotazioni)):
            if self.prenotazioni[i].cliente == cliente:
                del self.prenotazioni[i]
                break;
     
    def conta_biglietti_da_cliente(self, cliente):
        conta = 0
        for i in range(0, len(self.prenotazioni)):
            if self.prenotazioni[i].cliente == cliente:
                conta += 1

        return conta


p1 = Prenotazione(1000, "Mirco Rossi", "Bueno Camino", "2026-10-01 5:30", 2)
p2 = Prenotazione(1001, "Mirco Rossi", "Bueno Camino", "2026-10-01 5:30", 2)

c = Cinema()
c.inserisci_prenotazione(p1)
c.inserisci_prenotazione(p2)
print(c)
print(c.conta_biglietti_da_cliente("Mirco Rossi"))
c.rimuovi_da_id(1000)
c.rimuovi_da_cliente("Mirco Rossi")
