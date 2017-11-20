def main():
    song = 'Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you'.split(" ")
    n = int(input())
    persons = []
    for x in range(0, n):
        person = input().strip()
        persons.append(person)
    index = 0
    while True:
        if n <= 16:
            p = index % n
            print("{}: {}".format(persons[p], song[index]))
            index += 1
            if index == 16:
                break
        elif n > 16:
            p = index % 16
            print("{}: {}".format(persons[index % n], song[p]))
            index += 1
            if index % 16 == 0 and index > n:
                break
    
    
main()