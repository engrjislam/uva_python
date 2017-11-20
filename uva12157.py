def calculate_cost(duration, pulse, cost_per_pulse):
    cost = 0
    if duration <= 0:
        return 0
    total_pulse = int((duration / pulse))
    return total_pulse * cost_per_pulse + cost_per_pulse;

def main():
    test = int(input())
    mile_pulse, juice_pulse = 30, 60
    mile_cost, juice_cost = 10, 15
    case = 1
    while test > 0:
        calls = int(input())            
        durations = input().split(" ")
        mile, juice = 0, 0
        
        for duration in durations:
            mile += calculate_cost(int(duration), mile_pulse, mile_cost)
            juice += calculate_cost(int(duration), juice_pulse, juice_cost)
            
        if mile == juice:
            print("Case {}: Mile Juice {}".format(case, min(mile, juice)))
        elif mile < juice:
            print("Case {}: Mile {}".format(case, min(mile, juice)))
        elif mile > juice:
            print("Case {}: Juice {}".format(case, min(mile, juice)))
            
        case += 1
        test -= 1

main()