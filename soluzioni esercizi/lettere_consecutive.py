'''
Nella lingua italiana non esistono parole che hanno più di due lettere uguali consecutive.
Scrivere un algoritmo che, dato in input un array di 10 caratteri, stampi la parola “OK” se
e solo se l’array non contiene più di due caratteri uguali consecutivi.
Ad esempio, se v = ['m', 'a', 'm', 'm', 'a', 'a'] stampa "OK"; se 
v = ['a', 'l', 'b', 'b', 'b', 'e'] stampa "NO OK".
'''
# La parola letta in input, ovvero una stringa di caratteri, viene
# interpretata da Python come una lista (array) di catatteri.
a = input("Parola? ")

doppia = False
if len(a) > 2:
    for i in range(len(a)-2):
        if (a[i] == a[i+1] and a[i+1] != a[i+2]):
            doppia = True

else:
    if (len(a) == 2 and a[0] == a[1]):
        doppia = True
    else:
        doppia = False

if doppia == True:
    print("OK")
else:
    print("NO OK")

