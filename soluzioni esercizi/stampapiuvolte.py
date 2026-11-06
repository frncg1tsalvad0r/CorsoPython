'''
Scrivere un programma che, data una stringa e un numero intero N,
stampa la stringa passata come parametro N volte.

Scrivere il programma per verificare il corretto funzionamento della funzione.
'''
def stampa_piu_volte(stringa, N):
    #print(stringa*N)
    for i in range(0, N):
        print(stringa)


stampa_piu_volte('ciao', 9)
