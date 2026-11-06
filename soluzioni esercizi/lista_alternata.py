def intersecate(lista1,lista2):
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                
                return True
    return False
        
    
lista1=[9,7]  
lista2=[1,2,9,4,5]
print(intersecate(lista1,lista2))
