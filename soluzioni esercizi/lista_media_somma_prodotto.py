'''
Creare un programma che popola una lista con 20 numeri casuali (random) e che,
successivamente, tramite 3 funzioni che ricevono come parametro la lista, ne calcoli:
la somma, il prodotto e la media aritmetica. Stampare i risultati.

'''
import random
N = 20
MAX_RANDOM = 10

# Funzione che riceve come parametri la lunghezza, n, della lista da
# popolare con numeri casuali con valore massimo: max.
def popola_random(n, max):
    a = []
    for i in range(n):
        a.append(random.randint(0,max))
    return a

def somma(l,n):
    somma = 0
    for x in l:
        somma += x
    return somma

def prodotto(l,n):
    prodotto = 1
    for x in l:
        prodotto = prodotto * x
    return prodotto

def media(l,n):
    return somma(l,n)/n

l = popola_random(N, MAX_RANDOM)
print(l)
print(f"Somma = {somma(l,N)}")
print(f"Media = {media(l,N)}")
print(f"Prodotto = {prodotto(l,N)}")


