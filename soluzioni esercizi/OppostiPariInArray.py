'''
Si vuole scrivere un programma che legge dalla tastiera un N positivo intero.
Una volta letto genera un array di dimensione N con valori casuali (da 0 a 100).
Una volta costruito l’array trova tutti i numeri pari e ne cambia il segno
(2 PUNTI)

ESEMPIO:
Se N = 5 e i numeri casuali sono i seguenti

23 65 22 12 99

L’array finale diventerà

23 65 -22 -12 99

in quanto 22 e 12 sono pari
'''
import random
N = int(input("Inserire N "))
array = []
for i in range (0, N):
    casuale  = random.randrange(0, 101)
    array.append(casuale)

print(array)

# cambia il segno al pari
for i in range (0, N):
    if array[i] % 2 == 0:
        array[i] = -array[i]

print(array)
