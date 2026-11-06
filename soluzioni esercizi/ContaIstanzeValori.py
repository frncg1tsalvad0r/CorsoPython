'''Dato un array contare quante volte compare un numero
'''
def conta_istanze_valori(array,valore):
   conta=0
   for i in range(0,len(array)):
       if valore == array[i]:
           conta=conta+1
   return conta

a=[1,2,3,4,5,5]
print (conta_istanze_valori(a,5))


       
         
    
    
