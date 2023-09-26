from operator import itemgetter


def QW2(myFile):
    total = 0
    count = 0
    for line in myFile:
        if line != " ":
            total += len(line)
            count += 1
    mean = total / count
    print(mean)


def QW3():
    christmas = open("HW13 A Christmas Carol.txt", "r")
    chapters = {0: "", 1: "", 2: "", 3: "", 4: "", 5: ""}
    num = 0
    words = {}
    for line in christmas:
        line = line.replace("\n", " ")
        if line == "STAVE I:  MARLEY'S GHOST ":
            num = 1
        elif line == "STAVE II:  THE FIRST OF THE THREE SPIRITS ":
            num = 2
        elif line == "STAVE III:  THE SECOND OF THE THREE SPIRITS ":
            num = 3
        elif line == "STAVE IV:  THE LAST OF THE SPIRITS ":
            num = 4
        elif line == "STAVE V:  THE END OF IT ":
            num = 5
        else:
            chapters[num] += line

    for x in range(1, 6):
        new = ""
        for letter in chapters[x].lower():
            if ord("a") <= ord(letter) <= ord("z") or ord(letter) == 32:
                new += letter

        new = new.split(" ")
        QW2(new)
        for word in new:
            try:
                words[word] += 1
            except KeyError:
                words[word] = 1
    listOfWords = []
    for item in words:
        listOfWords.append([item, words[item]])
    listOfWords = sorted(listOfWords, key=itemgetter(1))[::-1]

    alphabetically = []
    for item in listOfWords:
        if item[1] == 1:
            alphabetically.append(item[0])
    print(sorted(alphabetically))

    longest = 0
    longestWord = ""
    for item in listOfWords:
        if len(item[0]) > longest:
            longestWord = item[0]
            longest = len(item[0])
    print(longestWord)


QW3()


