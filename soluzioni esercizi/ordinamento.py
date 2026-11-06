def separa(l, inizio, fine, indice_pivot):
    pivot = l[indice_pivot]
    l[indice_pivot], l[fine] = l[fine], l[indice_pivot]
    i = inizio
    f = fine

    while True:
        while(l[i]<=pivot):
            i+=1
        while(l[f]>pivot):
            f-=1
        if i < f:
            l[i], l[f] = l[f], l[i]
        else:
            break



l = [534,32,3,2423,43,55,234,12,2314,44,12]
print(l)
separa(l, 0, len(l)-1, 6)
print(l)