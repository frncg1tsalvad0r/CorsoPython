'''
Si vuole scrivere un programma che legge dalla tastiera un N positivo intero.
Una volta letto genera un array di dimensione N con valori casuali (da 0 a 100).
Una volta costruito l’array trova tutti i numeri dispari e ne cambia il segno
(2 PUNTI)

ESEMPIO:
Se N = 5 e i numeri casuali sono i seguenti

23 65 22 12 99

L’array finale diventerà

-23 -65 22 12 -99

in quanto 23, 65 e 99 sono dispari

'''
import random
N  = int(input("Inserisci un numero N "))
array  = []
for _ in range(0, N):
    casuale = random.randrange(0, 101)
    array.append(casuale)

print(array)

for i in range(0, N):
    if array[i] % 2 == 1:
        array[i] = -array[i]

print(array)
