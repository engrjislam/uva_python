
def main():
    test = int(input())
    while test > 0:
        string = ''.join(input().split())
        left_p = len(string.replace("(", ""))
        right_p = len(string.replace(")", ""))
        left_s = len(string.replace("[", ""))
        right_s = len(string.replace("]", ""))
        if len(string) % 2 != 0 or string.startswith(")") or string.startswith("]") or left_p != right_p or left_s != right_s:
            print("No")
            test -= 1
            continue
        for x in range(0, int(len(string) / 2) + 1):
            string = string.replace("()", "")
            string = string.replace("[]", "")
        if len(string) == 0:
            print("Yes")
        else:
            print("No")
        test -= 1
    

main()