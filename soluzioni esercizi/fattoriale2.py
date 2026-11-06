def esponente(M,N):
    if N==0:
        return 1
    return M*esponente(M,N-1)

m=int(input("inserisci un numero da elevare"))
n=int(input("inserisci esponente"))
print(esponente(m,n))
