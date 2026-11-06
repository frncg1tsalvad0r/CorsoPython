'''
Scrivi un programma che:
1. legge in input il valore della variabile x;
2. calcola e stampa il valore del polinomo di sesto grado: ax6 + bx5 + cx4 + dx3 + ex2 + f x + g, dove
i valori reali dei 7 coefficienti: a, b, c, d, e, f, g sono memorizzati in un file, coefficienti.txt (uno per
riga, oppure, tutti su un’unica riga)
'''
# Legge 7 coefficienti da coefficienti.txt (uno per riga)
file = open("coefficienti.txt", "r")
coefficienti = []
for riga in file:
    coefficienti.append(float(riga.strip()))
file.close()

a = coefficienti[0]
b = coefficienti[1]
c = coefficienti[2]
d = coefficienti[3]
e = coefficienti[4]
f = coefficienti[5]
g = coefficienti[6]

x = float(input("Inserisci il valore di x: "))

risultato = a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g
print("Valore del polinomio:", risultato)
