'''
uva: 11498
description: https://uva.onlinejudge.org/external/114/11498.pdf 
'''

def main():
    k = int(input())
    while k > 0:
        division_point = input().split(" ")
        m, n = int(division_point[0]), int(division_point[1])
        for test in range(k):
            xy_point = input().split(" ")
            x, y = int(xy_point[0]), int(xy_point[1])
            new_x, new_y = x - m, y - n
            
            if new_x == 0 or new_y == 0:
                print('divisa')
            elif new_x > 0 and new_y > 0:
                print('NE')
            elif new_x < 0 and new_y > 0:
                print('NO')
            elif new_x > 0 and new_y < 0:
                print('SE')
            elif new_x < 0 and new_y < 0:
                print('SO')
            
        k = int(input())
        
main()