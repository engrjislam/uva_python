import statistics

def main():
    numbers = []
    while True:
        try:
            number = int(input())
            numbers.append(number)
            print(int(statistics.median(numbers)))
        except(KeyboardInterrupt, ValueError, EOFError):
            break

main()