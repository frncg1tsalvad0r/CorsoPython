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
# Uso un dizionario per salvare i punteggi nella forma: domanda (chiave): punto (valore)
punteggio = {}

f = open("domande.csv", "rt")
for riga in f:
    riga = riga.strip()
    lista = riga.split(";")
    chiave = lista[0]
    valore = lista[1]
    #print(chiave)
    #print(valore)
    diz[chiave] = valore
    punteggio[chiave] = 0

concorrente = input("Prima di iniziare, dimmi il tuo nome: ")

for domanda in diz:
    #print(domanda)
    risposta = input(domanda + " ")
    #print(diz[domanda])
    if risposta.lower() == diz[domanda].lower():
        punteggio[domanda] = 1
        print("Risposta esatta!")
        #print(diz[domanda])
    else:
        print("Risposta errata!")
        punteggio[domanda] = -1
   
#print(diz)
g = open("risultati.txt", "at")
g.write(f"--- {concorrente} ----\n")

totale = 0
for domanda in punteggio:
    totale += punteggio[domanda]
    g.write(f"{domanda} {diz[domanda]}: {punteggio[domanda]}\n")
    
print(f"{concorrente}, hai ottenuto {totale} punti")
g.write(f"{concorrente}, hai ottenuto {totale} punti\n")
g.write("---------------------------------------------------------\n")

g.close()
f.close()
    
    
