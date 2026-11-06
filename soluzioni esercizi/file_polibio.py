import random as rnd

# Liste con l'alfabeto (tranne la lettera 'k')
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Una tabella è una lista di liste (le righe)   
def crea_tabella():
    m = []
    for i in range(5):
        m.append([])
        for j in range(5):
            m[i].append('')
    return m

# Metodo di estrazione che simula l'estrazione senza reinserimento (come nella "pesca");
# il carattere estratto viene poi rimosso dalla lista (remove)
def estrai_carattere():
    if len(alfabeto) > 0:
        # https://www.w3schools.com/python/ref_random_sample.asp
        r = rnd.sample(alfabeto,1)       
        #print(r[0])
        # https://www.w3schools.com/python/ref_list_remove.asp
        alfabeto.remove(r[0])
        return r[0]
    else:
        return ''

# Come il metodo precedente, solo che viene estratto non il carattere ma la sua posizione nella
# lista (randint) i restituito il carattere corrispondente;
# il carattere estratto viene poi rimosso dalla lista (del)
def estrai_carattere3(n):
    # https://www.w3schools.com/python/ref_random_randint.asp
    i = rnd.randint(0,n-1)
    ch = alfabeto3[i]
    #print(ch)
    # https://www.w3schools.com/python/ref_keyword_del.asp
    del alfabeto3[i]
    return ch

# Stampa la matrice del cifrario
def stampa_cifrario(m):
    print(" |1 2 3 4 5 |")
    print("-+----------+")
    for i in range(5):
        print(str(i+1) + '|', end = '')
        for j in range(5):
            print(m[i][j] + ' ', end = '')
        print("|")
    print("-+----------+")

# Funzione che restituisce il cifrario (matrice) usando la funzione estrai_carattere()          
def genera_cifrario(m):
    for i in range(5):
        for j in range(5):
            m[i][j] = estrai_carattere()
    return m

# Funzione che restituisce il cifrario (matrice) usando la funzione estrai_carattere3()  
def genera_cifrario3(m):
    n = 25
    for i in range(5):
        for j in range(5):
            m[i][j] = estrai_carattere3(n)
            n = n - 1
    return m

# Funzione che restituisce il cifrario (matrice) usando la funzione del modulo
# random "sample" (equivalentemente si poteva usare la funzione "shuffle").
def genera_cifrario2(m):
    # La funzione sample restituisce una lista con i 25 caratteri della lista "alfabeto2"
    # disposti casualmente.
    alfabeto_random = rnd.sample(alfabeto2, 25)
    for i in range(5):
        for j in range(5):
            m[i][j] = alfabeto_random[(5*i)+j]
    return m

# Salva il cifrario in un file il cui nome viene fornito come parametro; il cifrario
# viene salvato come una unica stringa di caratteri (senza "a capo")
def salva_cifrario(m, file):
    f = open(file, "wt")
    for i in range(5):
        for j in range(5):
            f.write(m[i][j])
    f.close()

# Salva il messaggio cifrato in un file il cui nome viene fornito come parametro
def salva_cifrato(msg, file):
    f = open(file, "wt")
    f.write(msg)
    f.close()

# Legge il cifrario da un file il cui nome viene fornito come parametro
def leggi_cifrario(file):
    f = open(file, "rt")
    # TODO: inserire un controlo di esitenza del file
    m = crea_tabella()
    for i in range(5):
        for j in range(5):
            m[i][j] = f.read(1)
            #print(f.read(1))
    f.close()
    return m

# Legge il messaggio da cifrare da un file il cui nome viene fornito come parametro
def leggi_messaggio(file):
    f = open(file, "rt")
    # TODO: inserire un controlo di esitenza del file
    msg = f.read()
    f.close()
    return msg

# Legge il messaggio da decifrare da un file il cui nome viene fornito come parametro
def leggi_cifrato(file):
    f = open(file, "rt")
    # TODO: inserire un controlo di esitenza del file
    msg = f.read()
    f.close()
    return msg

# Esegue la cifratura: ad ogni carattere vengono associate le sue coordinate (i+1, j+1)
# nella matrice del cifrario
def cifra(m, messaggio):
    cifrato = ""
    for ch in messaggio:
        #print(ch)
        esci = False
        for i in range(5):
            if esci:
                break
            for j in range(5):
                if ch == m[i][j]:
                    cifrato += str(i+1) + str(j+1)
                    esci = True
                    break

    return cifrato

# Esegue la decifratura: ad ogni coppia di coordinate viene associato il carattere corrispondente
# nella matrice del cifrario
def decifra(m, messaggio):
    decifrato = ""
    for i in range(0,len(messaggio)-1,2):
        #print(f"{messaggio[i]},{messaggio[i+1]}")
        decifrato += m[int(messaggio[i])-1][int(messaggio[i+1])-1]
    return decifrato


# Sezione di test

#msg = "ilgattomangialecrocchette"
#msg = input("Inserisci il messaggio da cifrare: ")

# Generazione di un cifrario e cifratura di un messaggio memorizzato in un file "chiaro_01.txt"
# quindi, salvataggio del messaggio cifrato e del cifrario in due dicersi file: "cifrato_01.txt", "cifrario_01.txt"
cifrario = genera_cifrario(crea_tabella())
stampa_cifrario(cifrario)
msg = leggi_messaggio("chiaro_01.txt")
cifrato = cifra(cifrario, msg)
salva_cifrato(cifrato, "cifrato_01.txt")
salva_cifrario(cifrario, "cifrario_01.txt")
print(f"chiaro = {msg}{'\n'}cifrato = {cifrato}")

##cifrario2 = genera_cifrario2(crea_tabella())
##stampa_cifrario(cifrario2)
##cifrato2 = cifra(cifrario2, msg)
##print(f"chiaro = {msg}{'\n'}cifrato = {cifrato2}")
##
##cifrario3 = genera_cifrario3(crea_tabella())
##stampa_cifrario(cifrario3)
##cifrato3 = cifra(cifrario3, msg)
##print(f"chiaro = {msg}{'\n'}cifrato = {cifrato3}")

# Decifratura del messaggio precedentemente cifrato e salvato in un file, anche il cifrario
# viene letto da un file.
cifrario = leggi_cifrario("cifrario_01.txt")
cifrato = leggi_cifrato("cifrato_01.txt")
decifrato = decifra(cifrario, cifrato)
print(decifrato)










                        

    
