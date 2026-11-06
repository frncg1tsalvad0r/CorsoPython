def elimina_duplicati(lista):
    nuova_lista=[]
    for i in range(len(lista)):
        trovato=False
        for k in range(len(nuova_lista)):
            if lista[i]==nuova_lista[k]:
                trovato=True
                
        if trovato==False:
            nuova_lista.append(lista[i])
            
    
    return nuova_lista

array=[1,1,2,3,3,3,4,5,6,6,6,7,7,7,8,9]
print(array)
print(elimina_duplicati(array))

