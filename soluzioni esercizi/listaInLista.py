'''
ESERCIZIO  ListaInLista
Scrivere un programma in python con una funzione che, date due liste di valori interi, verifichi che la sequenza della prima lista si trovi anche nella seconda lista restituendo la posizione della prima lista nella seconda altrimenti ritorna -1 se la prima lista non si trova nella seconda.
EX.
data la lista [3,6,4,8] e la lista [1,5,4,2,3,6,4,8,6,8]
la funzione ritorna 4 perché la sequenza della prima lista si trova, così com’è, nella seconda lista a partire dalla posizione 4 (zero based)
EX.
data la lista [3,6,4,8] e la lista [1,5,4,3,4,6,8]
la funzione ritorna -1 perché la sequenza della prima lista non si trova nella seconda.
'''

def lista_in_lista(l1, l2):
    if(len(l1)>len(l2)):
        return False;
    
    for i in range(0, len(l2)-len(l1)+1):
        if(l1[0] == l2[i]):
            # Trovato il primo valore; provo gli altri
            uguale = True
            for j in range (0, len(l1)):
                if(l1[j] != l2[i+j]):
                    uguale=False;
        
            if uguale ==  True:
                return True;

    return False;   

l1 = [1,2,3,4,7]
l2 = [9,2,3,4,6,1,2,3,4,7]
print(l1)
print(l2)
print(lista_in_lista(l1, l2))