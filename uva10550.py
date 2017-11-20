def main():
    while True:
        data = input()
        
        if data == '0 0 0 0':
            break
            
        i, f, s, l = data.split(" ")
        i, f, s, l = int(i), int(f), int(s), int(l)
        
        d = 3*360
        
        # every number adds 360 / 40 = 9 degree
        if i >= f:
            d += (i - f) * 9    
        else:
            d += (i%40 + 40 - f) * 9
        
        if f <= s:
            d += (s - f) * 9
        else:
            d += (40 - f + s%40) * 9
            
        if s >= l:
            d += (s - l) * 9
        else:
            d += (s%40 + 40 - l) * 9
        
        print(d)

main()