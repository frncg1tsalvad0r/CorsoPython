f = open("pippo", "r")
g=f.read(1)
while g != '':
    print(g)
    g=f.read(1)

f.close()
