def main():

    while True:
        n = input()
        if n == '0':
            break
        d = int(n[-1])
        x = int(n[:len(n)-1])
        diff = x - 5*d
        n = int(n)
        if n % 17 == 0 and diff % 17 == 0:
            print(1)
        else:
            print(0)


main()