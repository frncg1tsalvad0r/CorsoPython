"""
ESERCIZIO TrovaIlPiuFrequenteNellaSequenza
Data una sequenza di 20 numeri casuali da 1 a 5, cercare il numero che compare più volte all'interno della sequenza.
"""

def conta(l, val):
    c = 0
    for i in range(0, len(l)):
       if l[i] == val:
           c+=1
    return c


import random
l = []
for i in range(0,20):
    l.append(random.randrange(1,6))

print(l)

piu_frequente  = l[0]
frequenza = 0
for i in range(0, len(l)):
    c = conta(l, l[i])
    if c > frequenza:
       piu_frequente = l[i]
       frequenza = c

print("Il più frequente è ", piu_frequente, " e compare ", frequenza, "volte");
