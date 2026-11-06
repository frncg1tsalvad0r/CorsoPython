'''
Creare un programma che realizza un sistema di cifratura che fa corrispondere ad una lettera dell'alfabeto:
1 - una altra lettera di un secondo alfabeto nel quale le lettere sono disposte casualmente.
2 - (Cifrario di Atbash) una altra lettera di un secondo nel quale le lettere sono disposte dalla 'z' alla 'a'
'''
import random

alfa_chiaro = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfa_cifrato = []
LUN = len(alfa_chiaro)

def mescola(alfabeto):
 return random.sample(alfa_chiaro,LUN)

def inverti(alfabeto):
    invertito = []
    for i in range(LUN):
        invertito.append(alfa_chiaro[LUN-1-i])
    return invertito

def inverti2(alfabeto):
    # Vedi: https://www.w3schools.com/python/python_howto_reverse_string.asp
    return alfabeto[::-1]

print("a: cifratura con alfabeto mescolato\nb:cifratura con alfabeto invertito (Atbash) ")
scelta = input("scelta? ")
while (scelta != 'a' and scelta != 'b'):
    scelta = input("scelta? ")

if scelta == 'a':
    alfa_cifrato = mescola(alfa_chiaro)
else:
    alfa_cifrato = inverti(alfa_chiaro)

print("Alfabeto cifrante: " + str(alfa_cifrato))    

f = open("messaggio01.txt","rt")   
testo = f.read()
print("TESTO IN CHIARO: " + testo)
testo_cifrato = ""
for ch in testo:
    for i in range(LUN):
        if ch == alfa_chiaro[i]:
            testo_cifrato += alfa_cifrato[i]
            break
print("TESTO IN CIFRATO: " + testo_cifrato)
f.close()

