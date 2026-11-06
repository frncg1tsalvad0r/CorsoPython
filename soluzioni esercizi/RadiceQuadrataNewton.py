
c = float(input("Inserisci il numero per cui trovare la radice quadrata: "))

EPSILON = 1e-20
x0 = c + 1
x1 = (x0 + c / x0) / 2.0
while abs(x0-x1) > EPSILON:
    x0 = x1
    x1 = (x0 + c / x0) / 2.0

print (f"La radice quadrata di {c} è circa {x1}")