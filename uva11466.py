
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
        n = abs(int(input()))
        if n == 0:
            break
        primes = prime_factors(n)
        if n == 2 or len(primes) < 1:
            print(-1)
        else:
            print(primes[-1])


main()