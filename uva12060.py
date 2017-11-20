def dash(n):
    d = ''
    for x in str(n):
        d += '-'
    return d

def main():

    while True:
        numbers = input().split(" ")
        n = int(numbers[0])
        if n == 0:
            break
        sum = 0
        for number in numbers[1:]:
            sum += int(number)
        r = sum % n
        q = int(sum / n)
        print(sum / n)
        result = ''
        if r != 0:
            result = str(r) + '\n' + dash(n) + '\n' + str(n)
            #if q != 0:
            #    result = '\n' + str(q) + '\n' + result
        else:
            result = str(q)
        
        print(result)
        
        
main()