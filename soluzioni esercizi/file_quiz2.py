'''
Crea un programma che legga le diz da un file diz.txt.
Il file contiene righe nel formato:
domanda;risposta
Esempio:
Capitale d'Italia?;Roma
2+2?;4
Il programma deve:
    1. Leggere tutte le diz. 
    2. Fare il quiz all’utente. 
    3. Contare le risposte corrette. 
    4. Salvare il punteggio finale nel file risultati.txt
'''
# Uso un dizionario per memorizzare le righe del quiz (domanda;risposta) lette dal file
# nella forma: domanda (chiave): risposta (valore)
diz = {}

f = open("domande.csv", "rt")
for riga in f:
    riga = riga.strip()
    lista = riga.split(";")
    chiave = lista[0]
    valore = lista[1]
    #print(chiave)
    #print(valore)
    diz[chiave] = valore

concorrente = input("Prima di iniziare, dimmi il tuo nome: ")
g = open("risultati.txt", "at")
g.write(f"--- {concorrente} ----\n")
totale = 0
for domanda in diz:
    #print(domanda)
    risposta = input(domanda + " ")
    #print(diz[domanda])
    if risposta.lower() == diz[domanda].lower():
        totale += 1
        g.write(f"{domanda} {diz[domanda]}: risposta corretta\n")
        print("Risposta esatta!")
        #print(diz[domanda])
    else:
        print("Risposta errata!")
        totale += -1
        g.write(f"{domanda} {diz[domanda]}: risposta errata ({risposta})\n")
   
g.write(f"{concorrente}, hai ottenuto {totale} punti\n")
g.write(f"--- {concorrente} ----\n")
print(f"Punteggio ottenuto: {totale}")

g.close()
f.close()
    
    
