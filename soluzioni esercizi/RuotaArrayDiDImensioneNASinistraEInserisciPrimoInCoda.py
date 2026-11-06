'''
RuotaArrayDiDImensioneNASinistraEInserisciPrimoInCoda
Scrivere un programma che popola una lista di dimensione
N definita dall'utente con valori inseriti dall’utente.
Successivamente sposta tutti gli elementi della lista
verso sinistra (non si utilizzi una lista aggiuntiva)
ovvero mette quello che inizialmente era in seconda posizione,
lo mette in prima, quello che era in terza lo mette in seconda
e via dicendo.
Quello che era l’ultimo elemento viene messo in testa
'''
N = int (input("Inserisci N "))

array = []

for i in range (0, N):
    valore = int(input("Ineserisci un valore "))
    array.append(valore)

print(array)

#salvare il primo elemento della lista
tmp = array[0]

#sposto a sinistra
for i in range (0, N-1):
    array[i] = array[i+1]

# Inserisco l'elemento salvato in coda
array[N-1] = tmp

print(array)
