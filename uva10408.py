import fractions
from fractions import Fraction

def farey(n):
    items = []
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if fractions.gcd(x, y) == 1 and (x / y > 0 and x / y <= 1):
                items.append(x / y)
    return sorted(items)


def main():
    while True:
        try:
            inputs = input().split()
            numbers = [int(x) for x in inputs]
            n, k = numbers
            value = farey(n)[k-1]
            print(Fraction(value).limit_denominator())
        except(KeyboardInterrupt, ValueError, EOFError):
            break


main()