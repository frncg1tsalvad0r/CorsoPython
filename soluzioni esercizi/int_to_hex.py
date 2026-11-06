

def int_to_hex(decimale):
    ris = ""
    while True:
        r = decimale % 16
        if r <= 9:
            ris = str(r) + ris;
        elif r == 10:
            ris = "a" + ris;
        elif r == 11:
            ris = "b" + ris;
        elif r == 12:
            ris = "c" + ris;
        elif r == 13:
            ris = "d" + ris;
        elif r == 14:
            ris = "e" + ris;
        elif r == 15:
            ris = "f" + ris;
        decimale = decimale // 16
        if decimale ==0:
            break
    return "0x" + ris

print(int_to_hex(30))
