'''se lista è simmettrica o no'''

def array_simmetrico(array):
    metà=len(array)//2
    
    for i in range(0,metà):
        if array[i]!= array[len(array)-1-i]:
            return False
        return True
    

l=[1,2,3,3,2,1]
print(array_simmetrico(l))
            
            
            
        
        
        
    

