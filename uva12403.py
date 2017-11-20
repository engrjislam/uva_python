def main():
    test = int(input())
    total = 0
    while test > 0:
        data = input()
        
        if 'donate' in data:
            donate, amount = data.split(" ")
            total += int(amount)
        if 'report' in data:
            print(total)
        
        test -= 1

main()