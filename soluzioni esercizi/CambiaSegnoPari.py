def CambiaSegnoPari(lista):
    for i in range(len(lista)):
        if lista[i]%2==0:
            lista[i]=-lista[i]
    


array=[1,2,3,4,5,6,7,8,9,10]
print(array)
CambiaSegnoPari(array)
print(array)
