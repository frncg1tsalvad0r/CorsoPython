'''
Gestione parcheggio auto
'''
class Auto:
    targa=""
    marca=""
    modello=""
    disponibilita=False

    # COSTRUTTORE
    def __init__(self, t, ma, mo, d):
        self.targa  =t
        self.marca  =ma
        self.modello = mo
        self.disponibilita = d

    # RITORNA LA STRINGA DESCRITTIVA DELL'OGETTO
    def __str__(self):
        return self.targa + " " + self.marca + " " + self.modello + " " + str(self.disponibilita)
    
class Parcheggio:
    macchine = []

    # COSTUTTORE
    def __init__(self):
        pass

    # INSERISCI AUTO NEL PARCHEGGIO
    def inserisci_auto(self, auto):
        self.macchine.append(auto)

    # STRINGA DESCRITTIVA PARCHEGGIO
    def __str__(self):
        s = ""
        for i in range(0, len(self.macchine)):
            s += str(self.macchine[i]) + "\n"
        return s

    # INSERISCI AUTO NEL PARCHEGGIO
    def rimuovi_auto_da_targa(self, targa):
        for i in range(0, len(self.macchine)):
            if self.macchine[i].targa == targa:
                del self.macchine[i]
                return True
        return False
    
def stampa_menu():
    print("*************************")
    print("*******   MENU   ********")
    print("*************************")
    print("0) ESCI")
    print("1) VISUALIZZA AUTO")
    print("2) INSERISCI AUTO")
    print("3) RIMUOVI AUTO")
    print("*************************")

#PROGRAMMA PRINCIPALE

p= Parcheggio()
while True:
    stampa_menu()
    scelta = int(input("Scegli l'opzione>"))
    if scelta == 0:
        print ("********************************")
        print ("*** Esco dal programma. Bye. ***")
        print ("********************************")
        break
    elif scelta == 1:
        #visualizzo le auto
        print ("************************")
        print ("*** Visualizzo auto ***")
        print ("************************")
        print(p)
    elif scelta == 2:
        #inserisco auto
        print ("************************")
        print ("*** Inserimento auto ***")
        print ("************************")
        t = input("Inserisci la targa ")
        ma = input("Inserisci marca ")
        mo = input("Inserisci modello ")
        d = bool(input("Inserisci la diponibilita "))
        auto = Auto(t, ma, mo, d)
        p.inserisci_auto(auto)
        
    elif scelta == 3:
        #rimuovo auto
        print ("************************")
        print ("***** Rimuovi auto *****")
        print ("************************")
        t = input("Inserisci la targa dell'auto da rimuovere")
        if p.rimuovi_auto_da_targa(t) == True:
            print("Auto rimossa correttamete")
        else:
            print("Auto non trovata")
    
