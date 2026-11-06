#Un commerciante vende i suoi prodotti a prezzi scontati di una percentuale
#in base al prezzo:
#Per un prezzo < 50€ non  applica nessuno sconto,
#per un prezzo dai 50€ fino a 100€ escluso  applica uno sconto del 2%,
#mentre per un prezzo superiore ai 100€ applica uno sconto del 3%.
#Scrivere un programma in Python che legge il prezzo e stampa il valore scontato.

prezzo_iniziale = float(input("Inserisci prezzo"))
if prezzo_iniziale < 50:
    print ("Il prezzo è " + prezzo_iniziale);

if prezzo_iniziale >=50 and prezzo_iniziale <100:
    prezzo_finale = prezzo_iniziale - prezzo_iniziale/100*2
    print(prezzo_finale)

if prezzo_iniziale >= 100:
    prezzo_finale = prezzo_iniziale - prezzo_iniziale/100*3
    print(prezzo_finale)
