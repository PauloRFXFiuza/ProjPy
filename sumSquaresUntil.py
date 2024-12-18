'''
This function returns the sum of the natural numbers from 1 to n.
Examples: sumUntil(2) = 1 + 2= 3 ; sumSquaresUntil(4) = 1+2+3+4 =10 => sumUntil(n)=[n*(n+1)]/2
'''
def sumUntil(n):
    if  n >= 0:
        return ((n*(n+1))/2)
    else:
        print("Not a natural number!")

'''
This function returns the sum of the squares from 1 to n.
Examples: sumSquaresUntil(2) = 1² + 2²=1+4= 5 ; sumSquaresUntil(4) = 1+4+9+16 =30 => sumSquaresUntil(n) = ((n*(n+1)*(2*n+1))/6)
'''
def sumSquaresUntil(n):
    if  n >= 0:  
        return ((n*(n+1)*(2*n+1))/6)
    else:
        print("Not a natural number!")

print(sumUntil(2))
print(sumUntil(100))
print(sumUntil(-2))

print(sumSquaresUntil(2))
print(sumSquaresUntil(100))
print(sumSquaresUntil(-2))
