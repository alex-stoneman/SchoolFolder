from operator import itemgetter

UsedWords = ""
file = open("UsedWords.txt", "r")
for item in file:
    UsedWords += item
file.close()


# print(UsedWords)

def affine(text, common):
    listOfWords = []
    for y in [1, 3, 5, 7, 11, 15, 17, 19, 21, 23, 25]:
        for x in range(26):
            points = 0
            words = [""]
            word = ""
            for letter in text:
                char = ord(letter) - 97
                if 25 >= char >= 0:
                    char -= x
                    if char < 0:
                        char += 26
                    while char % y != 0:
                        char += 26
                    char = char // y
                char += 97

                word += chr(char)
            words += word
            listOfWords.append(words)
    triples(listOfWords, common)


def war():
    allWords = ""
    file = open("war_and_peace.txt", "r")
    for line in file:
        allWords = line
    file.close()

    common = {}
    current = allWords[:3]
    for letter in allWords:
        try:
            common[current] += 1
        except KeyError:
            common[current] = 1
        current = current[1:] + letter
    return common


def triples(possibliities, common):
    for possibility in possibliities:
        current = "0" + possibility[:2]
        for letter in possibility[2:]:
            current = current[1:0] + letter
            if current in common:
                pass


translate = ""
file = open("Encrypted.txt", "r")
for item in file:
    translate += item.lower()
file.close()
message = ""
for letter in translate:
    if ord("a") <= ord(letter) <= ord("z") or ord(letter) == 32:
        message += letter
message = message.split
common = war()
for item in message():
    affine(item, common)
