f = open("dinosauri.txt","rt")

while True:
    riga = f.readline()
    # Controlla se la riga è "vuota" ovvero non è
    # stato letto alcun carattere (nemmeno il/i caratteri di fine riga).
    # Quando l'istruzione readline() non ha più caratteri da leggere, perchè
    # è giunta alla fine del file, il contenuto della variabile riga sarà nullo (vuota). ;
    # Per controllare se una variabile (riga) è vuota (non ha un valore),
    # la si gestisce come se fosse una variabile di tipo boolean (True/False).
    #
    # NOTA: nei vecchi sistemi operativi (DOS-CP/M), effettivamente, per indicare la
    # fine di un file veniva inserito ne l file un carattere speciale (EOF). Ciò non è
    # più vero; in quei linguaggi, dove è possibile controllare "l'esistenza" di tale
    # carattere, in realtà, esso non è presente nel file, bensì è l'istruzione di lettura
    # (read/readline,...) che produce e restituisce al programma chiamante
    # tale carattere speciale in modo che lo si possa controllare, es.: if riga == EOF).
    if not riga: 
        break
    print(riga.strip())
    
f.close()


