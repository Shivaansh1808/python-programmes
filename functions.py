def readfile():

    filename = input("Enter The File Name that you want to read: ")
    numberofwords = 0
    file = open(filename, 'r')

    for line in file:
        words = line.split()
        print(len(words))
        numberofwords = numberofwords + len(words)

    print(numberofwords)

readfile()