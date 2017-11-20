def main():
    test = int(input())  # test cases
    while test > 0:
        data = input()
        a, b, c = 0, 0, 0
        for x in 'one':
            a += data.count(x)
        for x in 'two':
            b += data.count(x)
        for x in 'thre': #e
            c += data.count(x)
        if max(a, b, c) == a:
            print(1)
        elif max(a, b, c) == b:
            print(2)
        elif max(a, b, c) == c:
            print(3)
        test -= 1

main()