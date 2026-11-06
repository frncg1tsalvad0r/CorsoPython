'''
Creare un programma Python che esegue le seguenti funzioni:    
a) Creare una matrice 4x4 (4 righe, 4 colonne), inizialmente vuota.
b) Popolare la matrice con degli zeri, tranne gli elementi
che si trovano sulla diagonale, che dovranno contenere la somma
degli indici di riga e di colonna;
esempio: l'elemento di coordinate (3, 2) conterrà il valore 5.
c) Stampare tutti gli elementi della matrice (suggerimento per andare a
capo print(..., end="")).
d) Stampare gli elementi che si trovano sulla diagonale (quella che inizia
con l'elemento di coordinate (0, 0))  della matrice.
e) Stampare gli elementi che si trovano sopra la diagonale
della matrice (diagonale compresa).
f) Leggere in input un numero L, compreso tra 0 e 3, quindi stampare la sotto-matrice
di dimensione 3 ottenuta dalla matrice originale, togliendo la riga L e la colonna L (suggerimento: creare una nuova matrice...) 
'''
L = 4
# a)
m = [[],[],[],[]]

# Oppure:
m2 = [[]]*4
print(m2)

# Oppure:
m3 = []
for i in range(L):
    m3.append([])

# b
for i in range(L):
    for j in range(L):
        if i == j:
            m[i].append(i+j)
        else:
            m[i].append(0)
print("........................")

# c)
for i in range(L):
    for j in range(L):
        print(m[i][j], end="") 
    print()
print("........................")

# d)
for i in range(L):
    print(m[i][i], end="")
print()
print("........................")

# e)
for i in range(L):
    for j in range(i,L):
        print(m[i][j], end="")
    print()
print("........................")

# f)
n = int(input("Numero? "))
while(n<0 or n>L-1):
    n = int(input("Numero? "))
print(n)

m4 = []
for i in range(L):
    if i != n:
        r = []
        for j in range(L):
            if j != n:
                r.append(m[i][j])
        m4.append(r)

for i in range(L-1):
    for j in range(L-1):
        print(m4[i][j], end="")
    print()




