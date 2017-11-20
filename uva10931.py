'''
uva: 10931
description: https://uva.onlinejudge.org/external/109/10931.pdf
'''    
def main():
    
    while True:
        i = int(input())
        if i == 0:
            break
        bin = "{0:b}".format(i)
        parity = len(bin) - len(bin.replace('1', ''))
        print("The parity of {} is {} (mod 2).".format(bin, parity))
            
    
main()