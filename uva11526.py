'''
'''
import math
    
def main():
    test = int(input())
    while test > 0:
        n = int(input())
        print(n*math.log(n))
        test -= 1
        
main()
