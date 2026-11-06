'''
Creare un programma Python che calcola le frequenze relatice con
le quali i caratteri compaiono in un testo memorizzato in un file.
'''

# Un dizionario è una speciale lista, nella quale gli elementi non
# sono individuati da un indice numerico, bensì da una chiave (key)
# cioè una stringa alfanumerica; vedi: https://www.w3schools.com/python/python_dictionaries.asp
frequenze = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
    'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
    'y': 0, 'z': 0, 'à': 0, 'è': 0, 'é': 0, 'ì': 0, 'ò': 0, 'ù': 0
}
# Oppure, si può usare una litsa: frequenze = [0, 0, 0, 0, ...., 0] dove,
# per calcolare l'indice corrispondente al carattre, si può utilizzare la funzione
# ord(carattere) che restituisce un numero che parte da 97 (codice asci del carattere 'a'),
# quindi, l'indice corrispondente i = 97 - ord(carattere minuscolo);
# ad esempio, per il careattere 'a' i = 97 - ord('a') = 97 - 97 = 0

f = open("ariosto.txt", "rt", encoding="utf-8")

tot_caratteri = 0

# Salvo in una lista l'elenco delle chiavi
# vedi: https://www.w3schools.com/python/ref_dictionary_keys.asp
chiavi = frequenze.keys()
print(chiavi)

ch = f.read(1)
#while not ch == '':
while ch: # equivalente a while not ch == ''
    ch = f.read(1)
    # Per l'operatore in vedi: https://www.w3schools.com/python/python_operators_membership.asp
    #print(ch)
    if ch in chiavi:
        frequenze[ch] += 1
        tot_caratteri += 1

f.close()

print(f"Caratteri totali: {tot_caratteri}")
for ch in frequenze:
    print(f"{ch} {(frequenze[ch]/tot_caratteri)*100:.4f}")
            

