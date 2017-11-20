'''
uva: 10212
description: https://uva.onlinejudge.org/external/102/10212.pdf
'''

import math

def main():
    while True:
        try:
            numbers = input().split(" ")
            nums = []
            for x in numbers:
                if x != '':
                    nums.append(int(x))
            permutation = int(math.factorial(max(nums)) / math.factorial(max(nums) - min(nums)))
            last_non_zero_digit = 0
            while True:
                r = permutation % 10
                if r != 0:
                    last_non_zero_digit = r
                    break
                permutation //= 10
            
            print(last_non_zero_digit)
        except(KeyboardInterrupt, ValueError, EOFError):
            break    

main()