'''
Popolamento di una matrice con numeri casuali minori di 100
implementato mediante una funzione.
'''
import random

def popola_random(m, dim, max_random):
# Creo una matrice vuota ovvero una lista con N liste (vuote)
    for i in range(dim):
        m.append([])
        for j in range(dim):
            # Popolo la i-esima riga (lista vuota) con N numeri random
            m[i].append(random.randint(0,max_random))
    return m

def stampa_matrice(m, dim):
    for i in range(10):
        for j in range(10):
            # Uso la stringa di formato per tabulare con 5 posti per colonna
            # con allineamento a sinistra (<)
            print(f"{m[i][j]:<5}", end="")
        print()


m = []

# Creo una matrice vuota ovvero una lista con N liste (vuote)
for i in range(10):
    m.append([])
print(m)
print("---")

# Invoco la funzione passandogli la matrice vuota, la dimensione e il massimo
# valore casuale da generare
popola_random(m,10,100)
stampa_matrice(m,10)
print("---")
popola_random(m,10,100)
stampa_matrice(m,10)
print("---")
popola_random(m,10,100)
stampa_matrice(m,10)
    






    
