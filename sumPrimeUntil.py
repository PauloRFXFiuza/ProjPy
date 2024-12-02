'''
This function returns the sum of the squares from 1 to n.
Examples: sumSquaresUntil(2) = 1² + 2²=1+4= 5 ; sumSquaresUntil(4) = 1+4+9+16 =30
'''
def sumSquaresUntil(n):
    sum = 0
    if  n >= 0:
        for i in range(n+1):
            soma = soma + (i*i)
            return soma
    else:
        print("Not a natural number!")

    