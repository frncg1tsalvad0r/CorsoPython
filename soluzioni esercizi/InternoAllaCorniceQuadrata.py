#Un utente inserisce le coordinate di un punto
#nel piano e vuole sapere se si trovano all’interno
#dell’area delimitata da due quadrati
#rispettivamente di lato 2 e 4 con centro nell’origine.		(3 PUNTI)
x = float(input("X "))
y = float(input("Y "))

if ((x > 1 and x < 2) or (x < -1 and x > -2)) and \
    ((y > 1 and y < 2) or (y < -1 and y > -2)):
    print("dentro")
