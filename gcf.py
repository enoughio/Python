def GCF(n):


    i = 0
    x = n
    gcf = 1
    for i in range( 1, x + 1):
           if(n%i == 0):
                n = n//i   
                gcf = i * gcf
           else: 
                return gcf
    


a = 36
b = 60
print('the gcf is', GCF(34))
