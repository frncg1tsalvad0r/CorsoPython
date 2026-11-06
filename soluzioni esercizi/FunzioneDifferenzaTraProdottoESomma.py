
def differenza_somma_prodotto(x, y):
    '''
    FunzioneDifferenzaTraProdottoESomma
    Scrivere una funzione che calcoli il prodotto e
    la somma tra due numeri interi x e y e restituisce
    la differenza tra il prodotto e la somma.
    x un parametro
    y un pararmetro
    '''

    somma = x + y
    prodotto = x * y
    differenza = prodotto - somma;
    return differenza

print(differenza_somma_prodotto(10,2))

print(differenza_somma_prodotto(20,8))
