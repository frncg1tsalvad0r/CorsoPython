'''
Creare un programma a menu che gestisce un
dizionario italiano inglese

***************************************
***                  MENU         *****
***************************************
0) Programma termina
1) Inserisci una nuova coppia di valori
2) Cerca
3) Visualizza
4) Elimina parola
***************************************
'''
def stampa_menu():
    print("***************************************")
    print("***                  MENU         *****")
    print("***************************************")
    print("0) Programma termina")
    print("1) Inserisci una nuova coppia di valori")
    print("2) Cerca")
    print("3) Visualizza")
    print("4) Elimina parola")
    print("***************************************")
    return

dizionario = {}
while True:
    stampa_menu()
    opzione = input("Scegli l'opzione desiderata ")
    if opzione == "0":
        #Esce dal programma
        break
    elif opzione == "1":
        #Inserimento della coppia Inglese-Italiano
        inglese = input("Inserisci la parola in inglese ")
        italiano = input("Inserisci la parola in italiano ")
        dizionario[inglese] = italiano
        
    elif opzione == "2":
        #Cerca la parola nel dizionario
        '''
        inglese = input("Inserisci la parola in inglese ")
        print(dizionario[inglese])
        '''
        inglese = input("Inserisci la parola in inglese ")
        if inglese not in dizionario.keys():
            print ("Parola non trovata ")
        else:
            print (dizionario[inglese])
            
    elif opzione == "3":
        #Stampa tutto il dizionario
        print(dizionario)
        
    elif opzione == "4":
        #Elimina la parola dal dizionario
        inglese = input("Inserisci la parola in inglese ")
        if inglese in dizionario.keys():
            del dizionario[inglese]
        else:
            print("parola da cancellare non trovata")
        
        pass
    
print("Il programma è terminato Bye Bye!")    
