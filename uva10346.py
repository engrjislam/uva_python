def main():
    while True:
        try:
            numbers = input().split(" ")
            new_numbers = []
            for number in numbers:
                if number != '':
                    new_numbers.append(int(number))
            n, k = new_numbers
            sum = n
            while True:
                if n >= k:        
                    r = n % k
                    n = int(n / k)
                    sum += n
                    n = r + n
                else:
                    break
            print(sum)
        except(KeyboardInterrupt, ValueError, EOFError):
            break

main()