def media_da_file(file , n_col):
    somma=0
    n=0
    f = open(file,"r")
    for riga in f:
        n=n+1
        riga=riga.strip()
        #print(riga)
        l=riga.split("|")
        somma=somma+float(l[n_col])
        media=somma/n
        return media
    f.close() 


print(f"Temperatura media: {media_da_file('misure.csv',2)} gradi")
print(f"Pressione media: {media_da_file('misure.csv',3)} mbar")
print(f"Umidità media: {media_da_file('misure.csv',4)}%")




    
    



  
