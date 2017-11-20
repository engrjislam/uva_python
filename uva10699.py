'''
uva: 10699
description: https://uva.onlinejudge.org/external/106/10699.pdf
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
    return list(set(factors))
    
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print("{} : {}".format(n, len(prime_factors(n))))

main()