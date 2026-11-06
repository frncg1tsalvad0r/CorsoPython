class Libro:
    titolo = ""
    autore = ""
    anno = 0

    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def __str__(self):
        return "LIBRO: " + self.titolo + " " + self.autore + " " + str(self.anno)    


def stampa_menu():
    print("*****************************************")    
    print("************   MENU *********************")
    print("*****************************************")
    print("0) ESCI")
    print("1) VISUALIZZA LIBRI")
    print("2) INSERISCI LIBRO")
    print("3) RIMUOVI LIBRO")
    print("4) CERCA LIBRO")
    print("*****************************************")


class Libreria:
    libri = []

    def add_libro(self, libro):
        self.libri.append(libro)


    def elimina_libro(self, nome):
        for i in range(0, len(self.libri)):
            if self.libri[i].nome == nome:
                del self.libri[i]
                break

    def __str__(self):
        s = ""
        for i in range(0, len(self.libri)):
            s+= str(self.libri[i])  + "\n"
        return s
    
    def cerca_per_titolo(self, titolo):
        
        for i in range(0, len(self.libri)):
            if self.libri[i].titolo == titolo:
                return self.libri[i]
        return

#PRINCIPALE**************************************
libreria = Libreria()

while True:
    stampa_menu()
    scelta = int(input("SCEGLI>"))
    if scelta == 0:
        #esco
        print("Terminato")
        break
    elif scelta == 1: 
        #VISLUALIZZA LIBRI
        print("****************")
        print("VISUALIZZA LIBRI")
        print("****************")
        print(libreria)
        print("****************")
        
    elif scelta == 2:
        print("****************")
        print("INSERISCI LIBRO")
        print("****************")
        titolo = input("Titolo ")
        autore = input("Autore ")
        anno = int(input("Anno "))
        libro = Libro(titolo, autore, anno)
        libreria.add_libro(libro)

    elif scelta == 3:
        #elimina libro
        print("****************")
        print("RIMUOVI    LIBRO")
        print("****************")
        titolo = input("Titolo libro da cancellare")
        libreria.elimina_libro(titolo)

    elif scelta == 4:
        #ricerca libro
        print("*********************")
        print("CERCA LIBRO DA TITOLO")
        print("*********************")
        titolo = input("Titolo libro da cercare")
        libro_trovato = libreria.cerca_per_titolo(titolo)
        print(libro_trovato)
        
