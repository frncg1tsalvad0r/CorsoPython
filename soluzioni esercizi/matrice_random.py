'''
Popolamento di una matrice con numeri casuali minori di 100
'''

import random
N = 5
MAX = 100
# Creo una matrice vuota ovvero una lista con N liste (vuote)
for i in range(N):
    m.append([])
print(m)

for i in range(N):
    # Stampo le righe (liste vuote)
    print(m[i])
    for j in range(N):
        # Popolo la i-esima riga (lista vuota) con N numeri random
        m[i].append(random.randint(0,MAX))
    
# Stampiamo la matrice   
for i in range(N):
    for j in range(N):
        # Uso la stringa di formato per tabulare con 5 posti per colonna
        # con allineamento a sinistra (<)
        print(f"{m[i][j]:<5}", end="")
    print()



    
