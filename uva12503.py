def main():
    test = int(input())
    while test > 0:
        n = int(input())
        p = 0
        operations = []
        for x in range(0, n):
            pp = input().strip()
            if pp == 'LEFT':
                p -= 1
                operations.append(-1)
            elif pp == 'RIGHT':
                p += 1
                operations.append(1)
            elif 'SAME AS' in pp:
                ith = int(pp[7:]) - 1
                p += operations[ith]
                operations.append(operations[ith])
        print(p)
        test -= 1
    
    
main()