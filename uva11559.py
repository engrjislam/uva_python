'''
uva: 11559
description: https://uva.onlinejudge.org/external/115/11559.pdf 
'''

def main():

    while True:

        try:
            participants, budget, hotels, weeks = input().split(" ")
            
            participants = int(participants)
            budget = int(budget)
            hotels = int(hotels)
            weeks = int(weeks)
            
            costs = []
            
            while hotels > 0:
                price = int(input())
                beds = input().split(" ")
                for bed in beds:
                    bed = int(bed)
                    if bed >= participants and price * participants <= budget:
                        costs.append(price * participants)
                    
                hotels -= 1
            
            if len(costs) == 0:
                print('stay home')
            else:
                print(min(costs))    
        except(KeyboardInterrupt, EOFError):    
            break

            
main()