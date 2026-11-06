'''
scrivere una funzione che data una lista la ordina
'''
import random
import datetime

def bubble_sort(lista):
    n = len(lista)
    for j in range(0,n):
        for i in range(0,n-1):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                temp2 = lista[i+1]
                lista[i+1] = temp
                lista[i] = temp2
    return lista

def bubble_sort_sentinella(lista):
    n = len(lista)
    
    for j in range(0,n):
        modificato = False
        for i in range(0,n-1):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                temp2 = lista[i+1]
                lista[i+1] = temp
                lista[i] = temp2
                modificato = True
        if modificato == False:
            break
    return lista

            
            
            
        
n  = int(input("inserire limite lista "))
b = []

for i in range(0,n):
    r = random.random()
    a = round(r,2)
    b.append(a)
    #funzione round arrotonda
    #funzione math.trunc tronca che necessita della libreria math
    #math.ceil e math.floor
    
print(b)
inizio  =datetime.datetime.now()
bubble_sort_sentinella(b)
fine  =datetime.datetime.now()
print(fine-inizio)
print(b)



