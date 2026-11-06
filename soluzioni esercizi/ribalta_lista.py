'''
Creare un programma che crea un array di 10 elementi, assegnadogli poi dei valori casuali (Random)
dopo ci che si dovrà “ribaltare” l’array. 
Esempio: [3, 6, 7, 8, 4, 10, 13, 67, 72, 7] ==> [7, 72, 67, 13, 10, 4, 8, 7, 3, 6]
Suggerimento: se i indica la posizione di un elemento dell’array, 9-i quale posizione rappresenta?
Attenzione a quando i supera la metà.
'''
import random

# Funzione che riceve come parametri la lunghezza, n, della lista da
# popolare con numeri casuali con valore massimo: max.
def popola_random(n, max):
    a = []
    for i in range(n):
        a.append(random.randint(0,max))
    return a

# Funzione che riceve come parametro una lista e la sua lunghezza
# e ne restituisce una "ribaltata"
def ribalta(lista, n):
    for i in range(n//2):
        x = lista[i]
        # Il simmetrico dell'elemento di indice i è l'elemento di indice n-1-i
        print(str(i) + " - " + str(n-1-i))
        # Scambio usando una variabile di appoggio: x
        x = lista[i]
        lista[i] = lista[n-1-i]
        lista[n-i-1] = x
    return lista
    
l = popola_random(11, 100)
print(l)

print(ribalta(l,11))

