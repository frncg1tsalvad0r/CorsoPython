'''
Si vuole scrivere un programma che legge dalla tastiera un N positivo intero.
Una volta letto genera un array di dimensione N con valori casuali (da 0 a 100).
Successivamente viene cercato il minimo della sequenza e lo scambia con
quello che si trova nella posizione N//2  (2 PUNTI)

ESEMPIO:
Se N = 10 e i numeri casuali sono i seguenti
23 65 22 12 33 3 22 99 1 8

L’array finale diventerà
23 65 22 12 33 1 22 99 3 8
'''
import random
N  = int(input("Inserisci un numero N "))
array  = []
for _ in range(0, N):
    casuale = random.randrange(0, 101)
    array.append(casuale)

print(array)

minimo = array[0]
pos_minimo  =0
for i in range(0, N):
    if array[i] < minimo:
        minimo = array[i]
        posizione_minimo = i

#scambiare quello che si trova nella posizione_minimo con quello che si trova
# nella posizione N//2
tmp = array[posizione_minimo]
array[posizione_minimo] = array[N//2]
array[N//2] = tmp

print(array)
