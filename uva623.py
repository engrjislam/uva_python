'''
uva: 623
description: https://uva.onlinejudge.org/external/6/623.pdf
'''

import math


def main():
    while True:
        try:
            number = int(input())
            print("{}!".format(number))
            print(math.factorial(number))
        except(KeyboardInterrupt, ValueError, EOFError):
            break
            

main()