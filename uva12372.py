def main():
    test = int(input())
    case = 1
    while test > 0:
        data = input().split(" ")
        quality = "good"
        for x in data:
            if int(x) > 20:
                quality = "bad"
                break
        print("Case {}: {}".format(case, quality))
        case += 1
        test -= 1

main()