def main():
    test = int(input())
    while test > 0:
        inputs = input().split(" ")
        r, inputs = inputs[0], inputs[1:]
        sn = []
        for x in inputs:
            if x != "":
                sn.append(int(x))
        sn = sorted(sn)
        median = 0
        if len(sn) % 2 == 0:
            index = int(len(sn)/2)
            median = (sn[index-1] + sn[index]) / 2
        else:
            index = int(len(sn)/2)
            median = sn[index]
        sum = 0
        for x in sn:
            sum += abs(median - x)
        print(int(sum))
        test -= 1
    

main()