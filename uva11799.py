'''
uva: 11799
description: https://uva.onlinejudge.org/external/117/11799.pdf
'''

def main():
    tests = int(input())
    test = 1
    while tests > 0:
        line = input().split(" ")
        n = int(line[0])
        c = line[1:len(line)]
        max = int(c[0])
        for ci in c:
            ci = int(ci)
            if max < ci:
                max = ci
        print('Case {}: {}'.format(test, max))
        test += 1
        tests -= 1
        
        
main()