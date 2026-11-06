'''
Scrivi un programma che legga il file "nomi.txt" e crei un nuovo file
chiamato "nomi_filtrati.txt" contenente solo i nomi che hanno più di
4 caratteri (esclusi spazi iniziali/finali).
Stampa a schermo quanti nomi sono stati copiati nel nuovo file.
'''

def filtra_parole(file_nomi, file_nomi_filtrati, l_min):
    f1 = open(file_nomi)
    f2 = open(file_nomi_filtrati, "wt")
    # https://www.w3schools.com/python/ref_file_readlines.asp
    nomi = f1.readlines()
    n_filtrate = 0
    for nome in nomi:
        nome = nome.strip()
        if len(nome) > l_min:
            f2.write(nome + "\n")
        else:
            n_filtrate +=1
    f2.close()  
    f1.close()
    return n_filtrate

l_min = int(input("Lunghezza minima parola: "))
while l_min < 1 or l_min > 100:
    l_min = int(input("Lunghezza massima parola: "))

n_parole = filtra_parole("nomi.txt", "nomi_filtrati.txt", l_min)
print(f"Fatto! filtrate {n_parole}")
