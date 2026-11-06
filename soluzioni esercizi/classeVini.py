class Vino:
    nome = ""
    grado_alcolico = 0
    anno = 0
    tipo = ""

    #COSTRUTTORE viene invocato all'atto della costruzione
    def __init__(self, n, ga, a, t):
        self.nome = n
        self.grado_alcolico = ga
        self.anno = a
        self.tipo = t
    
    #STRINGA DESCRITTIVA viene invocato 
    def __str__(self):
        return "Nome: " + self.nome + " Grado Alcolico: " + str(self.grado_alcolico) + " Anno: " + str(self.anno) + " Tipo: " + self.tipo
    
    def inizializza(self, n, ga, a, t):
        self.nome = n
        self.grado_alcolico = ga
        self.anno = a
        self.tipo = t

    def is_alcolico(self):
        if self.grado_alcolico < 2:
            return True
        return False

class Cantina:
    vini = []

    def add_vino(self, vino):
        self.vini.append(vino)
        
    def rimuovi_vino_da_nome(self, nome):
        '''
        for v in self.vini:
        '''
        for i in range(0, len(self.vini)):
            if self.vini[i].nome == nome:
                del self.vini[i]
                return

        
    def __str__(self):
        s = ""
        for i in range(0, len(self.vini)):
            s+= str(self.vini[i]) + "\n"
        
        return s
    
    def ricerca_per_nome(self, nome):
        for i in range (0, len(self.vini)):
            if self.vini[i].nome == nome:
                return self.vini[i]

        return 
        
#PROGRAMMA PRINCIPALE
cantina = Cantina()
def stampa_menu():
    print("***************************************************")
    print("****************   MENU   *************************")
    print("***************************************************")
    print("0) ESCI DAL PROGRAMMA")
    print("1) INSERISCI VINO")
    print("2) VISUALIZZA VINI")
    print("3) RIMUOVI VINO DA NOME")
    print("4) RICERCA VINO DA NOME")
    print("***************************************************")


while True:
    stampa_menu()
    scelta = int(input("Scegli> "))
    if scelta == 0:
        print("Ciao grazie di aver partecipato")
        break
    elif scelta == 1:
        print("*******************")
        print("***AGGIUNGI VINO **")
        print("*******************")
        nome = input("Nome: ")
        grado_alcolico = int(input("Grado Alcolico: "))
        anno = int(input("Anno: "))
        tipo = input("Tipo: ")
        vino = Vino(nome, grado_alcolico, anno, tipo)
        cantina.add_vino(vino)
        
    elif scelta == 2:
        print("*******************")
        print("***VISUALIZZA VINI*")
        print("*******************")
        print(str(cantina))    
    elif scelta == 3:
        print("************************")
        print("***RIMUOVI VINI DA NOME*")
        print("***********************")
        nome = input("Inserisci il nome del vino da cancellare: ")
        cantina.rimuovi_vino_da_nome(nome)

    elif scelta == 4:
        print("************************")
        print("***CERCA VINI DA  NOME*")
        print("***********************")
        nome = input("Inserisci il nome del vino da cercare: ")
        print(cantina.ricerca_per_nome(nome))
        