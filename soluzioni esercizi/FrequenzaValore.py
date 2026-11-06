'''
data una lista, scrivere una funzione che determini
quante volte un valore
dato compare all'interno della lista stessa
'''
import random
def frequenza_valore(lista,valore):
    lunghezza_lista=len(lista)
    numero_valori=0
    for i in range(0,lunghezza_lista):
        if valore==lista[i]:
            numero_valori+=1

    return numero_valori

lista=[]

for i in range(0,20):
    valore_casuale=random.randrange(0,10)
    lista.append(valore_casuale)
valore=int(input("inserisci il valore"))
print(lista)


a = frequenza_valore(lista,valore)

print(a)


            
            

