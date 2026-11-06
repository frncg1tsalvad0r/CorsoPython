#Funzione Lista In Lista
def inserisci_in_crescenti(lista, val):
    lista.append(val)
    i = len(lista)-1
    for i in range(len(lista)-1, 0, -1):
        if lista[i] < lista[i-1]:
            lista[i], lista[i-1] = lista[i-1], lista[i]
        else:
            break
        
    return lista

l = [1,2,3,4,5,6,7,8,9,10,11]
print(l)
print(inserisci_in_crescenti(l, 16))
