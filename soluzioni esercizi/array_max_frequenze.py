'''
Creare un programma che assegna ad un array (lista) di 100
elementi dei valori casuali (random) minori di 30,
quindi, stampare in output il valore che nell’array
compare il maggior numero di volte.
'''
import random
        
a = []
for i in range(20):
    a.append(random.randint(0,30))
    #print(a[i])
print(a)

max = 0
n = 0
for i in range(20):
    cont = 0
    for j in range(20):
        if a[i] == a[j]:
            cont = cont + 1
        if cont > max:
            max = cont
            n = a[i]
        
        
    print("Il numero " + str(a[i]) + " è presente " + str(cont) + " volte.")

print(f"la frequenza massima è {max}")

