f=open('nomi.txt','w')
for i in range(0,6):
    nome=input('inserisci un nome')
    f.write(nome + '\n')
f.close()
