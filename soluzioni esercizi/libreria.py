class Libro:
    titolo=""
    autore=""
    anno=0

    def __init__(self, ti, au, an):
        self.titolo = ti
        self.autore = au
        self.anno = an

    def __str__(self):
        return self.titolo + ", " + self.autore + ", " + str(self.anno)



def stampa_menu():
    print("*********************************")
    print("******  LIBRERIA          *******")
    print("*********************************")
    print("0) ESCI")
    print("1) VISUALIZZA I LIBRI")
    print("2) INSERISCI LIBRO")
    print("3) RIMUOVI LIBRO")
    print("*********************************")

libreria = []
while True:
    stampa_menu()
    scelta=int(input("Scegli>"))
    if scelta == 0:
        #devo uscire
        print("Hai terminato l'applicazione. Goobye")
        break
    elif scelta == 1:
        #devo visualizzare tutti i libri della libreria
        if len(libreria) == 0:
            print("Non ci sono libri nella libreria")
        else:
            for l in libreria:
                print(l)
        
    elif scelta == 2:
        #inserisco il libro
        ti = input("Inserisci il titolo")
        au = input("Inserisci l'autore")
        an = int(input("Inserisci l'anno"))
        l = Libro(ti, au, an)
        libreria.append(l)
        
    elif scelta == 3:
        #rimuovo libro dalla libreria
        ti = input("Inserisci il titolo")
        for i in range(0, len(libreria)):
            if libreria[i].titolo == ti:
                del libreria[i]
                break
