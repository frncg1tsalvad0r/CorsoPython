'''
Scrivere un programma che popola una lista di dimensione N definita
dall'utente con valori casuali.
Successivamente, attraverso un ciclo sposta il più piccolo in coda
eseguendo la seguente procedura:
Controlla che il primo sia minore del secondo. Nel caso lo sia
scambia il primo con il secondo.
Controlla che il secondo sia minore del terzo. Nel caso lo sia
scambia il secondo con il terzo
Controlla che il terzo sia minore del quarto. Nel caso lo sia
scambia il terzo con il quarto.
…
La procedura continua finché si arriva all'ultimo elemento della
lista
EX:
Data una lista
[2, 5, 3, 1, 4, 7, 8] Scambio il 2 col 5 perché più piccolo
[5, 2, 3, 1, 4, 7, 8] Scambio il 2 col 3 perché più piccolo
[5, 3, 2, 1, 4, 7, 8] Il 2 e l’uno NON li scambio perchè 2 è più grande dell’uno
[5, 3, 2, 4, 1, 7, 8]  Scambio 1 con 4 perché più piccolo
[5, 3, 2, 4, 7, 1, 8]  Scambio 1 con 7 perché più piccolo
[5, 3, 2, 4, 7,  8, 1]  Scambio 1 con 8 perché più piccolo
Alla fine dell’iterazione il più piccolo si troverà in coda
'''
import random
N = int(input("Inserisci N" ))
lista = []
for i in range(0, N):
    casuale = random.randrange(1, 100)
    lista.append(casuale)
print(lista)

for i in range (0, N-1):
    if lista[i] < lista[i+1]:
        #scambiare lista[i] con lista[i+1]
        tmp = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = tmp

print(lista)  
