'''
Creare un programma che riceve in input un numero naturale (N>0) e che ne stampi
la sua rappresentazione binaria (al contrario: stampare direttamente i quozionti
ottenuti). Esempio: N=976; binario al contrario: 0000101111
'''

def converti(n):
    bin = []
    while n > 0:
        bin.append(n % 2)
        n = n // 2
    return bin

n = int(input("numero: "))
while n < 0:
    n = int(input("numero: "))

r = converti(n)

l = len(r)
for i in range(l):
    print(r[l-1-i], end='')
