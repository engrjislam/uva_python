import math 


def main():
    while True:
        try:
            numbers = input().split(" ")
            na = []
            for number in numbers:
                if number != '':
                    na.append(number)
            n, a = na
            n, a = int(n), int(a)
            sum = 0
            while n > 0:
                sum += n * int(pow(a, n))
                n -= 1
            print(sum)
        except(KeyboardInterrupt, ValueError, EOFError):
            break
    
main()