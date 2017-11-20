'''
uva: 10407
description: https://uva.onlinejudge.org/external/104/10407.pdf
'''

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(str(i))
    if n > 1:
        factors.append(str(n))
    return factors
    
def main():
    while True:
        n = int(input())
        if n == 0:
            break
            
        print(prime_factors(n))

main()