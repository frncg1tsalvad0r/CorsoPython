'''
Scrivere un programma che popola un array di dimensione N definito dall'utente con valori casuali.
Successivamente rovescia i valori della lista scambiando il primo elemento con l’ultimo, il secondo con il penultimo e via dicendo.
'''
import random
N = int(input("Inserisci un numero N "))

lista = []
for i in range (0, N):
    valore = random.randrange(1, 101)
    lista.append(valore)
    
print(lista)

'''
for i in range(0, N//2):
    temp = lista[i]
    lista[i] = lista[N-1-i]
    lista[N-1-i] = temp
'''

primo = 0
ultimo = N-1

while primo < ultimo:
    temp = lista[primo]
    lista[primo] = lista[ultimo]
    lista[ultimo] = temp
    primo += 1
    ultimo -= 1

    
print(lista)
