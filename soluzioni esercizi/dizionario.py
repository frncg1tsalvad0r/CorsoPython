'''
Gestire un dizionario
MENU
0) ESCI
1) VISUALIZZA DIZIONARIO
2) INSERISCI COPPIA ITALIANO_INGLESE
3) CERCA PAROLA
4) ELIMINA PAROLA
'''

def stampa_menu():
    print("********MENU*********");
    print("0) ESCI");
    print("1) VISUALIZZA DIZIONARIO");
    print("2) INSERISCI COPPIA ITALIANO_INGLESE");
    print("3) CERCA PAROLA");
    print("4) ELIMINA PAROLA");
    return


dizionario = {}
while True:
    stampa_menu()
    opzione = input("Scegli l'opzione desiderata: ")
    if opzione == "0":
        break
    
    elif opzione == "1":
        print(dizionario)
        
    elif opzione == "2":
        it = input("Inserisci il vocabolo italiano: ")
        en = input("Inserisci il vocabolo inglese: ")
        dizionario[it] = en
        
    elif opzione == "3":
        it = input("Inserisci il vocabolo italiano da cercare: ")
        #Scrivere la parte di codice che cerca la chiave e
        #se la trova ne stampa il valore corrispondente
        trovato = False
        for chiave in dizionario.keys():
            if chiave == it:
                #trovata
                en = dizionario[it]
                print(f"Il significato di {it} è {en}")
                trovato = True
                break

        if trovato == False:
            print("non trovato")
        
     
    else:
        print ("Opzione non valida.... ")

print("Bye !")
