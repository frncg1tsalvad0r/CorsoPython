#Funzione Lista In Lista
def conta_primi(lista):
    conta = 0
    for i in range(len(lista)):
        primo = True
        for divisore in range(2, lista[i]):
            if lista[i] % divisore == 0:
                primo=False
                break
        if primo:
            print(lista[i])
            conta += 1
    return conta

l = [1,2,3,4,5,6,7,8,9,10,11]
print(l)
print(conta_primi(l))
