N = 10
v = [3, 5, 2, 7, 8, 1, 4, 9, 6, 0]
def p ():

    for i in range (1, N-1):
        if (v[i-1]>v[i]):
            t=v[i-1]
            v[i-1]=v[i]
            v[i]=t
	
p()

print(v)
