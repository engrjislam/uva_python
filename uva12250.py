def main():
    test = 0
    while True:
        language = input()
        if language == '#':
            break
        elif language == 'HELLO':
            language = "ENGLISH"
        elif language == 'HOLA':
            language = "SPANISH"
        elif language == 'HALLO':
            language = "GERMAN"
        elif language == 'BONJOUR':
            language = "FRENCH"
        elif language == 'CIAO':
            language = "ITALIAN"
        elif language == 'ZDRAVSTVUJTE':
            language = "RUSSIAN"
        else:
            language = "UNKNOWN"
        test += 1
        print("Case {}: {}".format(test, language))

main()