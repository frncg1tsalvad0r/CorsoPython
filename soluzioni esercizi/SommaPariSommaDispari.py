'''Creare una lista di n casuali 20 e poi fare una somma fra i numeri pari
e i numeri dispari'''
import random

lista=[]
somma_pari=0
somma_dispari=0
for i in range(20):
    lista.append(random.randrange(0, 100))
for i in range(20):
    if lista[i]%2==0:
        somma_pari+=lista[i]
    
    else:
        somma_dispari+=lista[i]

print(lista)
print(f"La somma dei numeri pari è: {somma_pari}")
print(f"La somma dei numeri dispari è:{somma_dispari}")

    
