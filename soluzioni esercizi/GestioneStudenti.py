class Studente:
    matricola = ""
    nome = ""
    eta = ""

    #COSTRUTTORE
    def __init__(self, m, n, e):
        self.matricola = m
        self.nome = n
        self.eta = e


    #STRINGA DESCRITTIVA
    def __str__(self):
        return self.matricola + " " + self.nome + " " + str(self.eta)

class Classe:
    studenti = []

    #COSTRUTTORE
    def __init__(self):
        pass

    #STRINGA DESCRITTIVA DELLA CLASSE
    def __str__(self):
        s = ""
        for i in range(0, len(self.studenti)):
            s += str(self.studenti[i]) + "\n"
        return s

    #AGGGIUNEGRE UNO STUDENTE NELLA CLASSE
    def aggiungi_studente(self, s):
        self.studenti.append(s)

    #RIMUOVERE UNO STUDENTE DATA LA SUA MATRICOLA
    def rimuovi_studente_da_matricola(self, mat):
        for  i in range(0, len(self.studenti)):
            if self.studenti[i].matricola == mat:
                del self.studenti[i]
                return True
        return False
    
c = Classe()
def stampa_menu():
    print("****************************")
    print("*******   CLASSE ***********")
    print("****************************")
    print("0) ESCI")
    print("1) VISUALIZZAZIONE CLASSE")
    print("2) INSERISCI STUDENTE")
    print("3) RIMUOVI STUDENTE")
    print("****************************")

c = Classe()

#PRINCIPALE
while True:
    stampa_menu()
    scelta = int(input("SCEGLI: "))
    if scelta == 0:
        #ESCO DAL PROGRAMMA
        print("*******************")
        print("Programma Terminato")
        print("*******************")
        break
    elif scelta == 1:
        #VISUALIZZO GLI STUDENTI
        print("*******************")
        print("Visualizzo Studenti")
        print("*******************")
        print(c)
    elif scelta == 2:
        #INSERISCI STUDENTE
        print("*******************")
        print("Inserisco Studente")
        print("*******************")
        m = input("Inserici la matricola ")
        n = input("Inserisci il nome ")
        e = int(input("Inserisci eta "))
        stud = Studente(m, n, e)
        c.aggiungi_studente(stud)
    elif scelta == 3:
        #RIMUOVI STUDENTE
        print("**********************************")
        print("Rimuovo Studente data la matricola")
        print("**********************************")
        m = input("Inserici la matricola da rimuovere> ")
        if c.rimuovi_studente_da_matricola(m)== True:
            print("Studente rimosso correttamete")
        else:
            print("Studente non rimosso")
    
