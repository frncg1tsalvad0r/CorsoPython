def rovescia(lista):
    for i in range(len(lista)//2):
        lista[i], lista[len(lista)-1-i]= lista[len(lista)-1-i], lista[i]
    return


array=[1,2,3,4,5]
print(array)
rovescia(array)
print(array)
        
