'''
Scrivere una funzione che, data una lista di numeri,
cambia il segno dei massimi. (2 PUNTI)

ESEMPIO:
Se la lista fosse la seguente
23 65 22 22 33 4 22 99 8
la funzione cambia il segno a 99 e la lista modificata sarà
23 65 22 22 33 4 22 -99 8

ESEMPIO:
Se la lista fosse la seguente
23 65 88 22 33 4 22 88 8
la funzione cambia il segno a tutti i numeri 88
23 65 -88 22 33 4 22 -88 8
'''
def cambia_segno_massimi(lista):
    massimo = lista[0]
    for i in range(0, len(lista)):
        if lista[i] > massimo:
            massimo = lista[i]
    for i in range(0, len(lista)):
        if lista[i] == massimo:
            lista[i] *= -1
    return lista

a = [23, 65, 22, 22, 33, 4, 22, 65, 8]
print(a)
cambia_segno_massimi(a).append(6)
print(a)
    
