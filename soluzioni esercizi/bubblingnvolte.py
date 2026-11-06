'''
Si vuole scrivere una funzione che, data una lista e un numero
intero N (minore della dimensione della lista) esegue
il bubbling in coda del numero più grande per N volte. 
Scrivere il programma per verificare il corretto
funzionamento della funzione. (1.5 PUNTI)
'''

def bubbling_N(lista, n):

    for i in range(0, n):
        #facciamo il bubbling del più grande
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j+1]:
                tmp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = tmp
