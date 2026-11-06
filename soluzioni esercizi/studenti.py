class Studente:
    matricola = 0
    nominativo = ""
    classe = ""

    def __init__(self, ma, no, cl):
        self.matricola  =ma
        self.nominativo = no
        self.classe = cl

    def __str__(self):
        return str(self.matricola) + ", " + self.nominativo + ", " + self.classe



def stampa_menu():
    print("***********************")
    print("****** MENU     *******")
    print("***********************")
    print("0) ESCI DAL PROGRAMMA")
    print("1) VISUALIZZA STUDENTI")
    print("2) INSERISCI STUDENTE")
    print("3) RIMUOVI STUDENTE")

studenti = []
while True:
    stampa_menu()
    scelta = int(input("Scelgli l'opzione>"))

    if scelta==0:
        #ESCI
        print("IL PROGRAMMA E' TERMINATO")
        break
    elif scelta == 1:
        #VISUALIZZO STUDENTI
        if len(studenti) == 0:
            print ("Studenti in vacanza")
        else:
            for s in studenti:
                print(s)
                
    elif scelta == 2:
        # INSERISCO UNO STUDENTE
        ma = int(input("Inserisci la matricola "))
        no = input("Inserisci nominativo ")
        cl = input("Inserisci classe")
        s = Studente(ma, no, cl)
        studenti.append(s)

    elif scelta == 3:
        # RIMUOVO STUDENTE
        ma = int(input("Inserisci la matricola da rimuovere "))
        for i in range(0, len(studenti)):
            if studenti[i].matricola == ma:
                del studenti[i]
                break;
            
