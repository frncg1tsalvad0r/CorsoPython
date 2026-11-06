class Libro:
    titolo = ""
    autore = ""
    anno = 0

    #COSTRUTTORE
    def __init__(self, t, au, an):
        self.titolo = t
        self.autore = au
        self.anno = an

    #STRINGA DESCRITTIVA
    def __str__(self):
        return self.titolo + " " +self.autore + " " + str(self.anno)


class Libreria:
    libri = []

    #COSTRUTTORE
    def __init__(self):
        pass

    #STRINGA DESCRITTIVA
    def __str__(self):
        s = ""
        for i in range(0, len(self.libri)):
            s += str(self.libri[i]) + "\n"

        return s

    # Inserisco un libro nella libreria        
    def aggiungi_libro(self, l):
        self.libri.append(l)

    # Rimuovere un libro
    def rimuovi_libro_da_titolo(self, t):
        for i in range(0, len(self.libri)):
            if self.libri[i].titolo == t:
                del self.libri[i]
                return True
        return False
    
def stampa_menu():
    print("*****************************")
    print("******** LIBRERIA   *********")
    print("*****************************")
    print("0)  ESCI")
    print("1)  VISUALIZZA LIBRI")
    print("2)  INSERISCI LIBRO")
    print("3)  RIMUOVI LIBRO")
    print("*****************************")

libreria = Libreria()
while True:
    stampa_menu()
    opzione = int(input("SCEGLI L'OPZIONE"))
    if opzione == 0:
        print("*********************************")
        print("Programma terminato, Arrivederci ")
        print("*********************************")
        break
    elif opzione == 1:
        #VISUALIZZO I LIBRI
        print("**********************")
        print("   VISUALIZZO LIBRI ")
        print("**********************")
        print(str(libreria))

    elif opzione == 2:
        #INSERISCO LIBRO
        print("**********************")
        print("   INSERISCO LIBRO ")
        print("**********************")
        t = input("Inserisci il titolo del libro ")
        au = input("Inserisci l'autore ")
        an = int(input("Inserisci l'anno "))

        libro = Libro(t, au,an)
        libreria.aggiungi_libro(libro)
        
    elif opzione == 3:
        #RIMUOVI LIBRO
        print("**********************")
        print("   RIMOZIONE LIBRO ")
        print("**********************")
        t = input("Inserisci il titolo del libro da cancellare")
        if libreria.rimuovi_libro_da_titolo(t) == True:
            print("Libro cancellato correttamente")
        else:
            print("Libro non cancellato")
        
