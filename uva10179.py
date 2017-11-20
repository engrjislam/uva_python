'''
'''

import fractions

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))
    
def main():
    '''
    while True:
        n = int(input())
        if n == 0:
            break
        count = 1
        for x in range(2, n):
            if fractions.gcd(x, n) == 1:
                count += 1
    '''
    n = int(input())   
    print(prime_factors(n))

main()