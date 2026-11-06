'''
Scrivere un programma che, dopo aver letto un numero intero N da tastiera ne stampa la sua forma binaria.
Per calcolare il numero binario di un numero decimale si procede con una serie di divisioni intere e
con il calcolo del resto.
'''

N = int(input("Inserisci un numero intero positivo: "))

divisione_intera = N // 2
while divisione_intera != 0:
    resto = N % 2
    print(resto, end="")
    N = divisione_intera
    divisione_intera = divisione_intera // 2