def gcd(a, b):
    
    while a != b:
        if a > b:
            a -= b  
        else:
            b -= a  
    return a  

a = 48
b = 18
print('Greatest Common Divisor (GCD) of two numbers:',gcd(a, b))  
