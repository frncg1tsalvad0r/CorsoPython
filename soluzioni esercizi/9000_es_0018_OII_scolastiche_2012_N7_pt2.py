def f(n):
    k=2
    while ((k*k <= n) and (n % k != 0)):
        k = k+1
    if (k*k > n): 
        return 1 
    else: 
        return 0

print(f(11))