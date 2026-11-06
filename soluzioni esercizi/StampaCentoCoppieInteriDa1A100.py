#Scrivere un programma che stampa a video 100 numeri interi nella seguente sequenza:
# 1 100 2 99 3 98 4 97 ……………………………………..99 2 100 1

i = 1
while i <= 100:
    print(i)
    print(101-i)
    i+=1