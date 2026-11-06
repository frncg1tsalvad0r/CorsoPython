'''
Si vuole scrivere un programma che legge dalla tastiera un N positivo intero.
Una volta letto genera un array di dimensione N con valori casuali (da 0 a 100).
Successivamente viene cercato il massimo della sequenza e lo scambia con quello
che si trova nella posizione posizione N//2  (2 PUNTI)

ESEMPIO:
Se N = 10 e i numeri casuali sono i seguenti
23 65 22 12 33 3 22 99 1 8

L’array finale diventerà
23 65 22 12 33 99 22 3 1 8
'''
import random
N = int(input("Inserisci il valore di N "))
array=[]
for i in range(0, N):
    casuale = random.randrange(0,101)
    array.append(casuale)

print(array)

massimo = array[0]
posizione_massimo = 0
for i in range(0, N):
    if array[i] > massimo:
        massimo = array[i]
        posizione_massimo=i

tmp = array[posizione_massimo]
array[posizione_massimo] = array[N//2]
array[N//2] = tmp

print(array)
