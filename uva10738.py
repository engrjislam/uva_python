'''
uva: 10738
description: https://uva.onlinejudge.org/external/107/10738.pdf
'''

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
    return factors
    
def unique_prime_factors(primes):
    return list(set(primes))
    
def is_squire_free(n):
    primes = prime_factors(n)
    unique_primes = unique_prime_factors(primes)
    if len(primes) - len(unique_primes) == 0:
        return True
    return False
    
def mu(n):
    if n == 1:
        return 1
    if not is_squire_free(n):
        return 0
    elif is_squire_free(n) and len(prime_factors(n)) % 2 == 0:
        return 1
    else:
        return -1

def m(n):
    sum = 0
    while n >= 1:
        sum += mu(n)
        n -= 1
    return sum
    
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print('{:>8}{:>8}{:>8}'.format(n, mu(n), m(n)))

main()