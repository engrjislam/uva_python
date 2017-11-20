'''
uva: 10338
description: https://uva.onlinejudge.org/external/103/10338.pdf
'''
import math

def count_same_chars(message):
    count = []
    while message != '':
        total = len(message)
        message = message.replace(message[0], '')
        new_total = len(message)
        if total - new_total > 1:
            count.append(total - new_total)
            
    return count

def main():
    test = int(input())
    index = 1
    while test > 0:
        message = input()
        result = math.factorial(len(message))
        for x in count_same_chars(message):
            result /= math.factorial(x)
        print('Data set {}: {}'.format(index, int(result)))
        index += 1
        test -= 1
        
main()
