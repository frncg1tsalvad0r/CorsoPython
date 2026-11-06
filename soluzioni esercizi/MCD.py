def massimo_comun_divisore(a, b):
    while True:
        resto = a%b
        if resto == 0:
            MCD = b
            break
        a = b
        b = resto
    a = 1000;
    return MCD


x = int(input("Inserire il primo valore "))
y = int(input("Inserire il secondo valore "))

print(f"Stampo il MCD tra {x} e {y}")




print ("Il MCD è ", massimo_comun_divisore(x, y))
print(x)
