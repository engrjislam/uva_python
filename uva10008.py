def main():
    test = int(input())
    data = ''
    while test > 0:
        string = ''.join(input().split())
        string = ''.join([c for c in string if not c.isdigit() and c.isalpha()])
        data += string
        test -= 1
    data = data.lower()    
    chars = set(data)
    chars_list = []
    for char in chars:
        count = data.count(char)
        chars_list.append((char.upper(), count))
        data = data.replace(char, "")
    chars_list.sort(key=lambda x: x[0])
    chars_list.sort(key=lambda x: x[1], reverse=True)
        
    for (x, y) in chars_list:
        print("{} {}".format(x, y))

main()