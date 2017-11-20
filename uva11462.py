
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        inputs = input().split()
        numbers = sorted([int(x) for x in inputs])
        string = ' '.join([str(number) for number in numbers])
        print(string)


main()