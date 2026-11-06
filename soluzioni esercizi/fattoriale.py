def fattoriale (N):
    fattoriale=1
    for i in range(1,N+1):
        fattoriale*=i

    return fattoriale

n=int(input("inserisci un numero"))
print(fattoriale(n))

        
