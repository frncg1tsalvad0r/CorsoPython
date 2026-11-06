#Funzione ContaGruppi

def conta_gruppi(lista):
    conta = 0
    numerosita = 1
    for i in range(1, len(lista)):
        
        if lista[i-1] == lista[i]:
            numerosita += 1
        else:
            if numerosita >=2 :
                conta+=1
            numerosita = 1

    return conta

l = [1,2,3,4,5,6,7,8,8,8,8,0,9,9,10,11,11,0]

print(l)
print(conta_gruppi(l))
