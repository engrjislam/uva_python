import math


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
    
def main():
    while True:
        try:
            number = int(input())
            if is_prime(number):
                n = int(str(number)[::-1])
                if is_prime(n) and n != number:
                    print("{} is emirp.".format(number))
                else:
                    print("{} is prime.".format(number))
            else:
                print("{} is not prime.".format(number))
        except(KeyboardInterrupt, ValueError, EOFError):
            break
            

main()