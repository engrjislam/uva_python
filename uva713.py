def main():
    test = int(input())
    while test > 0:
        numbers = input().split(" ")
        sum = 0
        for number in numbers:
            sum += int(number[::-1])
            
        print(int(str(sum)[::-1]))
        
        test -= 1

        
main()