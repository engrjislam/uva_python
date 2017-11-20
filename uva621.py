def main():
    test = int(input())
    s = ['1', '4', '78']
    while test > 0:
        data = input()
        
        if data == s[0] or data == s[1] or data == s[2]:
            print('+')
        elif (data.startswith(s[0]) or data.startswith(s[1]) or data.startswith(s[2]):
            print('-')
        elif not (data.startswith(s[0]) and data.endswith(s[0]) or data.startswith(s[1]) and data.endswith(s[1]) or data.startswith(s[2]) and data.endswith(s[2])):
            print('*')
        elif data.endswith(s[0]) or data.endswith(s[1]) or data.endswith(s[2]):
            print('?')
        
        test -= 1

main()