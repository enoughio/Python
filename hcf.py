def HCF(n, m):
    smaller = min(n, m)

    i = 0
    for i in range( 1, smaller + 1):
           if(n%i == 0):
                n = n//i   
           else: 
                hcf =  i-1
                break
    
    return hcf



a = 36
b = 60

print("The Highest Common Factor of", a, "and", b, "is", HCF(a, b))

