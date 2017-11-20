'''
uva: 573
description: https://uva.onlinejudge.org/external/5/573.pdf
'''

def count_day(ih, dc, sd, ff, wh):

    '''
    day -> max day to climb or fall
    ih  -> initial height
    dc  -> distance climbed
    hac -> height after climbing
    has -> height after sliding
    sd -> slide down
    ff -> the fatigue factor expressed as a percentage
    '''
    
    day = 1
    
    while True:
    
        hac = round(ih + dc, 2)
        has = round(hac - sd, 2)
        
        print(day, ' --- ', ih, ' --- ', dc, ' --- ', hac, ' --- ', has)
        
        if has < 0 or hac > wh:
            break
            
        day += 1
        ih = has
        dc = round((1 - ff / 100) * dc, 2)
    
    if has < 0:
        return day, 'failure'
        
    return day, 'success'

def main():
    
    while True:
    
        '''
        h -> the height of the well in feet     #   h=0 >>> terminate the program
        u -> the distance in feet that the snail can climb during the day
        d -> the distance in feet that the snail slides down during the night
        f -> the fatigue factor expressed as a percentage
        
        hints:  
            (1) all four numbers (h, u, d, f) will be between 1 and 100, inclusive
            (2) if the fatigue factor drops the snail’s climbing distance below zero, 
                the snail does not climb at all that day
            (3) regardless of how far the snail climbed, it always slides d feet at night
        '''
        
        h, u, d, f = input().split(' ')
        h, u, d, f = int(h), int(u), int(d), int(f)
        
        if h <= 0:
            break
            
        day, status =  count_day(0, u, d, f, h)  
        print('{} on day {}'.format(status, day))
        
        
main()
