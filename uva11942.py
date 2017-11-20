def main():
    test = int(input())
    fst = test
    while test > 0:
        l = input().split(" ")
        
        x = []
        for p in l:
            try:
                x.append(int(p))
            except(ValueError):
                pass
        
        y = list(reversed(x))
        
        if fst == test:
            print('Lumberjacks:')
        
        if all(x[i] <= x[i+1] for i in range(len(x)-1)) or all(y[i] <= y[i+1] for i in range(len(y)-1)):
            print('Ordered')
        else:
            print('Unordered')
        
        test -= 1

main()