def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def main():
    
    string = input()
    string = string.split(" ")
    numbers = []
    for s in string:
        if not s == '':
            numbers.append(int(s))
    
    days, dd, mm, yyyy = numbers
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap_year(yyyy):
        days_in_month[1] = 29
        
    dd = (dd + days) % days_in_month[mm - 1]
    
    print(dd)
    
main()