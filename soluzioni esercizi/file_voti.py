'''
Scrivi un programma che:
1. Chieda all'utente di inserire il nome e il voto (intero da 1 a 10)
   di un numero a piacere di studenti. L'inserimento termina quando
   l'utente digita "fine" come nome.
2. Salvi i dati in un file "voti.txt" nel formato: Nome,Voto
3. Al termine, legga il file appena creato e stampi a schermo:
   - La lista degli studenti con i loro voti
   - La media della classe
   - Il nome dello studente con il voto più alto
'''

def salva_voti(file):
    n = 0
    f = open(file, "wt")
    while True:
        nome = input("Nome studente (o fine per terminare): ")
        if nome == "fine":
            break
        voto = int(input("Voto: "))
        f.write(f"{nome}, {voto}\n")
        n += 1
        
    f.close()
    return n

def leggi_voti(file):
    max = -1
    tot = 0
    n = 0
    nome = ""
    f = open(file, "rt")
    for riga in f:
        n += 1
        riga = riga.strip()
        print(riga)
        l = riga.split(",")
        voto = int(l[1])
        tot += voto
        if voto > max:
            max = voto
            nome = l[0]
    print(f"Media classe: {tot/n}")
    print(f"Voto massimo: {max} - {nome}")
    f.close()
         
n = salva_voti("voti.txt")
print(f"Letti {n} voti)")
leggi_voti("voti.txt")
