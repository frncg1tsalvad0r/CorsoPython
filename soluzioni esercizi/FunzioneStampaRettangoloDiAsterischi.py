'''
Scrivere una funzione che, dati due parametri interi R e C,
stampa un quadrato di asterischi  alto R e largo C.
'''
def stampa_rettangolo_asterischi(R, C):
    #stampare ad una ad una le righe
    for r in range (0, R):

        #Stampo ad una ad una le colonne di asterisci
        for c in range(0, C):
            print("*", end="")

        #vado a capo
        print();
        
R = 10
stampa_rettangolo_asterischi(R, 4);

stampa_rettangolo_asterischi(3, 3);


