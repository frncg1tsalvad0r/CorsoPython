'''
Crea un programma che:
1. legga numeri interi dal file numeri.txt (un numero per riga);
2. separi i numeri pari dai dispari;
3. salva i numeri pari nel file pari.txt e i numeri dispari nel file dispari.txt.
'''
file = open("numeri.txt", "r")
pari = []
dispari = []
for riga in file:
    n = int(riga.strip())
    if n % 2 == 0:
        pari.append(n)
    else:
        dispari.append(n)
file.close()

file_pari = open("pari.txt", "w")
for n in pari:
    file_pari.write(str(n) + "\n")
file_pari.close()

file_dispari = open("dispari.txt", "w")
for n in dispari:
    file_dispari.write(str(n) + "\n")
file_dispari.close()

print("Pari:", pari)
print("Dispari:", dispari)
