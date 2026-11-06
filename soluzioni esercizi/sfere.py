'''
Una macchina che controlla la produzione di sfere per cuscinetti
in modo che siano della dimensione di 5 mm di diametro con un errore
del 1% (cioè nell’intervallo [5 mm - 1%, 5 mm +1%] ).
Scrivere un programma che, inserito il diametro misurato (float) stabilisca
se il pezzo è da tenere o da scartare. (2 PUNTI)
'''

d=float(input("inserisci un numero"))
if d<=(5+1/100*5) and d>=(5-1/100*5):
    print("il diametro è da tenere")
else:
    print("il diametro è da scartare")


