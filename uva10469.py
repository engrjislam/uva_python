def bin_xor_to_int(a, b): return int(a,2) ^ int(b,2)

def main():
    while True:
        try:
            numbers = input().split(" ")
            a, b = ['{0:b}'.format(int(x)) for x in numbers]
            print(bin_xor_to_int(a, b))
        except(KeyboardInterrupt, ValueError, EOFError):
            break

main()