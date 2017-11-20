def main():
    test = int(input())
    while test > 0:
        n = int(input())
        r = str(int((n * 567 / 9 + 7492) * 235 / 47 - 498))
        print(r[-2])
        test -= 1
    

main()