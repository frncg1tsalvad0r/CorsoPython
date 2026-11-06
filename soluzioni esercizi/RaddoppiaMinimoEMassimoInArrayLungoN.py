'''
Dato un array di valori casuali
Moltiplica per 2 il massimo e il minimo di un array

'''
import random
N = int (input("inserisci un numero N intero di valori "))
array = []
for i in range(0, N):
    dato = random.randrange(0, 101)
    array.append(dato)

print(array)
pos_min = 0
pos_max = 0
max = array[0]
min = array[0]

for i in range(0, N):
    if array[i] < min:
        min = array[i]
        pos_min = i
        
    if array[i] > max:
        max = array[i]
        pos_max = i


print ("Minimo ", min)
print ("POS Minimo ", pos_min)

print ("Massimo ", max)
print ("POS Massimo ", pos_max)


array[pos_min] *= 2
array[pos_max] *= 2

print (array)

