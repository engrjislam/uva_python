def main():
    test = int(input())  # test cases
    while test > 0:
        n = int(input()) # observed days
        p = int(input()) # number of parties
        h = []
        for x in range(0, p):
            h.append(int(input())) # hartal parameters
        days = [] # hartal days
        fridays = [6] 
        nfds = int(n / 7) # number of fridays
        for x in range(1, nfds):
            fridays.append(6 + x * 7)
        for x in h:
            index = 1
            nn = int(n / x)
            for xx in range(1, nn + 1):
                if (x * index) % 7 != 0 and x * index <= n and (x * index) not in fridays:
                    days.append(x * index)
                index += 1
        print(len(set(days)))
        test -= 1

main()