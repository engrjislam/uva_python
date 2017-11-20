'''
uva: 583
description: https://uva.onlinejudge.org/external/5/583.pdf
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
        result = ''
        if n < 0:
            result = '-1 x '
        result = str(n) + ' = ' + result + ' x '.join(prime_factors(abs(n)))
        print(result)

main()