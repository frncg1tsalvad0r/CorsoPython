#Scrivere un programma che stampa a video 100 numeri interi che sono la somma 
# dei due precedenti (esclusi i due numeri 1 che non sono somma dei due precedenti).
# Il primo numero  è 1 e il secondo 1.
# La sequenza è
# 1 1 2 3 5 8 13 21 34 etc
# Di questi numeri solo i pari dovranno essere stampati ovvero
# 2 8 43 etc
prec = 1
prec_prec = 1

print(prec_prec);
print(prec);

i = 0
while i < 98:
    attuale = prec + prec_prec
    if attuale%2 == 0:    # Il numero è pari
        print(attuale)
    prec_prec = prec
    prec = attuale
    i += 1