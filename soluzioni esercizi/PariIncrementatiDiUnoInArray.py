'''
Si vuole scrivere un programma che legge dalla tastiera un N positivo intero.
Una volta letto genera un array di dimensione N con valori casuali
(da 0 a 100).
Una volta costruito l’array trova tutti i numeri pari e ne incrementa
il valore di 1  (2 PUNTI)

ESEMPIO:
Se N = 5 e i numeri casuali sono i seguenti

23 65 22 12 99

L’array finale diventerà

23 65 23 13 99

in quanto 22 e 12 sono pari e quindi diventano rispettivamente 23 e 13
'''
import random
N = int(input("Inserisci il valore di N "))
array=[]
for i in range(0, N):
    casuale = random.randrange(0,101)
    array.append(casuale)

print(array)

for i in range(0, N):
    if array[i] % 2 == 0:
        #pari
        array[i] +=1

print(array)
