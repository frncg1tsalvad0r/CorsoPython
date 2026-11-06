class Auto:
    targa=""
    marca=""
    modello=""
    potenza=0

    def __init__(self, ta, ma, mo, po):
        self.targa = ta
        self.marca = ma
        self.modello = mo
        self.potenza = po

    def __str__(self):
        return "Auto: " + self.targa + "," + self.marca \
               + "," + self.modello  \
                        + "," + str(self.potenza)

def stampa_menu():
    print("********************************")
    print("***     GESTORE NOLEGIO    *****")
    print("********************************")
    print("0) ESCI")
    print("1) VISUALIZZA AUTOMOBILI")
    print("2) INSERISCI AUTOMOBILE")
    print("3) RIMUOVI AUTOMOBILE")

automobili  = []
while True:
    stampa_menu()
    scelta  = int(input("Scegli opzione>"))
    if scelta == 0:
        #Esci dal programma
        print("Ciao ciao ")
        break
    
    elif scelta == 1:
        #visualizza automobili
        for a in automobili:
            print(a)
            
    elif scelta == 2:
        #inserisco automobile
        tg = input("Inserisci la targa")
        mr = input("Inserisci la marca")
        mo = input("Inserisci modello")
        pt = float(input("Inserisci la potenza"))
        a = Auto(tg, mr, mo, pt)
        automobili.append(a)
    elif scelta == 3:
        tg = input("Inserisci la targa")
        for i in range(0, len(automobili)):
            if automobili[i].targa == tg:
               del automobili[i]

                
        pass
