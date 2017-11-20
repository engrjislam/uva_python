
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
 
def sum_digits(n):
    sum = 0
    while n > 0:
        m = n % 10
        sum += m
        n -= m
        n //= 10
 
    return sum
 
def add_prime_factors(n):
    sum = 0
    for i in prime_factors(n):
        sum += sum_digits(i)
 
    return sum

    
def main():
    test = int(input())    
    while test > 0:
        m = int(input())
        while True:
            m += 1            
            if len(prime_factors(m)) > 1 and sum_digits(m) == add_prime_factors(m):
                print(m)
                break
        test -= 1
            

main()