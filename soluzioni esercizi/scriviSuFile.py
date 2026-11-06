scelta = input("Scrivi (s) o leggi (l)");
if scelta == 's':
    f = open("file1.txt", 'w')
    f.write("Lorem,ipsum")
    f.close()

elif scelta == 'l':
    f = open("file1.txt", 'r')
    r = f.readline()
    r.split(',')
    print(r)

    pass

