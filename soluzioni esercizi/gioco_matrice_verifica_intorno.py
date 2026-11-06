'''
Gioco: 
a) Creare uma matrice 10x10 i cui elementi contengono il carattere blank: '+' spazio.
b) Assegnare a 10 celle, le cui coordinate sono state scelte casualmente, il carattere 'O' (il bersaglio).
c) Il gioco chiede ripetutamente al giocatore di indovinare (tiro) le coordinate (riga, colonna)
del bersaglio che verranno lette in input (ciclo while).
Il gioco termina quando la prima coordinata è un numero negativo.
d) Per ogni coordinata inserita, il programma deve verificare se il giocatore:
ha centrato un bersaglio, assegnando al giocatore 8 punti, oppure se il tiro è caduto nell’intorno
di una cella con il bersaglio, assegnando 1 punto.
L’intorno di una cella è costituito dalle 8 celle che la contornano; attenzione alle celle sui bordi
della matrice.
e) Il gioco finisce, con un messaggio che informa il giocatore del punteggio ottenuto, quando
il giocatore ha centrato tutti i bersagli, oppure come si è detto al punto c).
'''
# Importo la libreria random
import random

m = []
N_RIG = 10
N_COL = 10
N = 10

# Creo la matrice assegnando il caratte '+' (blank) a tutte le celle 
for i in range(N_RIG):
    m.append([])
    for j in range(N_COL):
        m[i].append('+')

# Assegno N caratteri 'O' in posizioni casuali (indice di riga e di colonna, numeri random)
for i in range(N):
    r = random.randint(0,N_RIG-1)
    c = random.randint(0,N_COL-1)
    m[r][c] = 'O'
    
# Stampo la matrice
for i in range(N_RIG):
    for j in range(N_COL):
        print(m[i][j], end="") 
    print()
    
punteggio = 0

# Coordinate della cella da controllare (ad esempio, la cella (2, 2))
while True:
    print("premi f per terminare")
    x = input("riga? ")
    y = input("colonna? ")
    # Controllo se il giocatore vuole terminare il gioco
    if x == 'f' or y == 'f':
        break
    # Converto i valori letti in interi
    x = int(x)
    y = int(y)
    # Verifico che le coordinate siano valide
    if x < 0 or x >= N_RIG or y < 0 or y >= N_COL:
        print("Coordinate fuori dalla matrice")
    else:
        # Se la cella centrale ha il valore 1, non facciamo nulla
        if m[x][y] == 'O':
            punteggio = punteggio + 100

        # Controllo la cella "sopra a sinistra"
        x1 = x-1
        y1 = y-1
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1  

        # Controllo la cella "sopra"
        x1 = x-1
        y1 = y
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1            
        # Controllo la cella "sopra a destra"
        x1 = x-1
        y1 = y+1
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1
        # Controllo la cella "a sinitra"
        x1 = x
        y1 = y-1
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1
        # Controllo la cella "a destra"
        x1 = x
        y1 = y+1
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1
        # Controllo la cella "sotto a sinistra"
        x1 = x+1
        y1 = y-1
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1
        # Controllo la cella "sotto"
        x1 = x+1
        y1 = y
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1
        # Controllo la cella "sotto a destra"
        x1 = x+1
        y1 = y+1
        if (x1 >= 0 and x1 < N_RIG) and (y1 >= 0 and y1 < N_COL):
            if m[x1][y1] == 'O':
                punteggio = punteggio + 1

        print(f"Il punteggio ottenuto è: {punteggio}")  

print("Finito!")   

