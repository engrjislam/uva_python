def main():
    test = int(input())
    case = 1
    while test > 0:
        numbers = input().split(" ")
        n = int(numbers[0])
        numbers = numbers[1:]
        new_numbers = []
        for number in numbers:
            new_numbers.append(int(number))
        new_numbers.sort()
        print('Case {}: {}'.format(case, new_numbers[int(n/2)]))
        test -= 1
        case += 1

main()