'''
Creare un programma che legge in input una sequenza di numeri e che, dopo
ogni input, stampi la differenza tra l’ultimo letto ed il penultimo
(per il primo numero letto si supponga che il “penultimo” abbia valore 0).
Esempio: 10, 14, 6, 8 , 4, 9, 22, 8, 32, 12,
deve stampare: 10, 4, -8, 2, -4, 5, 13, -14, 24, -20.
'''

u = int(input("Numero 1 "))
while u > 0:
    p = u
    u = int(input("Numero 2 "))
    print(u-p)
