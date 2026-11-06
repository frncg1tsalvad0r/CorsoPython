'''Si vuole scrivere un programma che legge dalla tastiera degli interi
maggiori di zero e termina quando l’utente inserisce un valore negativo.
Alla fine dell’inserimento si vuole stampare il valore massimo inserito
(l’ultimo valore inserito non è considerato). (2 PUNTI)
'''
max=n=int(input("inserisci un numero"))
while n>=0:
    if n>max:
        max=n
    n=int(input("inserisci un valore"))
print(max)

    
    
    
    

