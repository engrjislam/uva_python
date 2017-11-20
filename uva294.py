'''
uva: 294
description: https://uva.onlinejudge.org/external/2/294.pdf
'''

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def count_factors(x):
    return len(list(factors(x)))
    
def main():
    test = int(input())
    while test > 0:
        inputs = input().split(" ")
        numbers = []
        for i in inputs:
            if i != '':
                numbers.append(int(i))
        x, y = numbers
        x, y = min(x, y), max(x, y)
        max_count = 0
        num = 0
        for n in range(x, y + 1):
            if max_count < count_factors(n):
                max_count = count_factors(n)
                num = n
        print("Between {} and {}, {} has a maximum of {} divisors.".format(x, y, num, max_count))
        test -= 1

main()