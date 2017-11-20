def main():
    while True:
        a, b = input().split(' ')
        a, b = int(a), int(b)
        if a == -1 and b == -1:
            break
        if a == 0:
            a == 100
        if b == 0:
            a == 100
        zap = min(min(a, 100 - a) + min(b, 100 -b), abs(a - b))
        print(zap)
    
    
main()