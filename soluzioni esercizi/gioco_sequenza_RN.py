'''
Popolare, in modo casuale (random), un array (lista in Python) di 20 elementi con le sole lettere
R (rosso) e N (nero), quindi (fare un programma per ognuno dei segunti punti):
a. determinare la più lunga sequenza continua della lettera R
b. determinare la più lunga sequenza continua della lettera R e della lettera N
c. [gioco] simulare il seguente gioco: generare un numero casuale non superiore alla lunghezza
dell’array, se l’elemento che si trova nella posizione (indice) corrispondente al numero estratto
corrisponde alla lettera R allora il giocatore acquisisce un punteggio pari alla lunghezza della
sequenza alla quale la lettera appartiene; esempio: se l’array è il seguente [R,R,R,N,N,R,N,N,N,R,R,R,R,N,N]
e, se il numero estratto è 11, allora il punteggio acquisito sarà 4 perché la lettera R, in posizione 11,
appartiene ad una sequenza di 4 lettere R.
'''

# Importo la libreria random
import random

# Definisco "a" come una lista vuota, quindi non viene alloca la memoria necessaria
a = []
LUN = 20

for i in range(LUN):
    if random.randint(0,100) > 80:
        a.append("R")
    else:
        a.append("N")
    #a[i] = random.randint(0,30) non va bene perchè la memoria non è stata assegnata

print(a)

p = int(input("Posizione? "))

punteggio = 1

# Controllo le posizioni successive ad a[p]
i = p
while(i < len(a)-1 and a[i] == a[i+1]):
    print(i)
    punteggio = punteggio + 1
    i = i + 1

# Controllo le posizioni precedenti ad a[p]
i = p
while(i > 0 and a[i] == a[i-1]):
    print(i)
    punteggio = punteggio + 1
    i = i - 1

print(f"il punteggio ottenuto è {punteggio}")

