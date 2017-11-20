def main():
    while True:
        try:
            eqation = input()
            print(eqation)
        except(KeyboardInterrupt, EOFError):
            break

main()