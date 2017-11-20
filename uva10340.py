def main():
    while True:
        try:
            s, t = input().split(" ")
            if t.find(s) == 0 or s in t:
                print("Yes")
                continue 
            count = 0
            for ss in s:
                if ss in t:
                    t = t[t.index(ss) + 1:]
                    #print(t)
                    count += 1
            if len(s) == count:
                print("Yes")
            else:
                print("No")
        except(KeyboardInterrupt, ValueError, EOFError):
            break

main()