'''
SpostaArrayDiDImensioneNASinistra
Scrivere un programma che popola una lista di dimensione N definita
dall'utente con valori che devono essere inseriti dall’utente.
Successivamente sposta tutti gli elementi della lista verso
sinistra ovvero mette quello che inizialmente era in prima
seconda posizione, lo mette in prima, quello in terza lo mette
in seconda e così via.
Quello che era il primo elemento viene perso
'''
N = int(input("Inserisci un numero N "))
array = []

for i in range(0, N):
    valore = int(input("Iserisci il valore"))
    array.append(valore)

print(array)

for i in range(0, N-1):
    array[i] = array[i+1]

print (array)
