'''
'''
def baseN(num, b, numerals="0123456789ABCDEF"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def convert(number, from_base, to_base):
    return baseN(number, to_base)
    
print(convert(12, 10, 11))