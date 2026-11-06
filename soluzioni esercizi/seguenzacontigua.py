'''ESERCIZIO  PiuContiguo
Scrivere una funzione che, data una lista di
numeri interi, restituisca il numero che
compare nel gruppo contiguo più numeroso
(se ci sono gruppi con la stessa numerosità ritornerà
uno dei gruppi)
ESEMPIO:
Se ho una lista 
[1,3,7,4,9,9,3,5,5,5,8,2]
la funzione ritorna il valore 5 perché 5 appartiene
al gruppo contiguo più numeroso
Verificare il funzionamento della funzione popolando
una lista con dei dati a piacere.'''
import random
def seguenza_contigua(lista):
    conteggio=1
    conteggio_maggiore=1
    valore_conteggiato_maggiore=lista[0]
    for i in range (1, len(lista)):
        if lista[i]==lista[i-1]:
            conteggio+=1
        else:
            conteggio=1
        if conteggio>conteggio_maggiore:
            conteggio_maggiore=conteggio
            valore_conteggiato_maggiore=lista[i]
    return(conteggio_maggiore, valore_conteggiato_maggiore)
lista=[]
for i in range(0,20):
    lista.append(random.randrange(0, 5))
print(lista)
print(seguenza_contigua(lista))

            
            
    
