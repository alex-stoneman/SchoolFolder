from operator import itemgetter

AllWords = []
file = open("Words.txt", "r")
for item in file:
    AllWords.append(item[:-1].lower())
file.close()
UsedWords = ""
file = open("UsedWords.txt", "r")
for item in file:
    UsedWords += item
file.close()
# print(UsedWords)
letterFrequencies = {
    "E": 11.1607, "M": 3.0129,
    "A": 8.4966, "H": 3.0034,
    "R": 7.5809, "G": .4705,
    "I": 7.5448, "B": 2.0720,
    "O": 7.1635, "F": 1.8121,
    "T": 6.9509, "Y": 1.7779,
    "N": 6.6544, "W": 1.2899,
    "S": 5.7351, "K": 1.1016,
    "L": 5.4893, "V": 1.0074,
    "C": 4.5388, "X": 0.2902,
    "U": 3.6308, "Z": 0.2722,
    "D": 3.3844, "J": 0.1965,
    "P": 3.1671, "Q": 0.1962
}


def affine(text):
    listOfWords = []
    for y in [1, 3, 5, 7, 11, 15, 17, 19, 21, 23, 25]:
        for x in range(26):
            points = 0
            words = [[], 0]
            for i in text:
                word = ""
                for letter in i:
                    char = ord(letter)
                    if ord("z") >= char >= ord("a"):
                        char = (char - x)//y
                        while char > ord("z"):
                            char -= 26
                    word += chr(char)
                words[0].append(word)
            for i in words[0]:
                if i in AllWords:
                    words[1] += 1
            for i in words[0]:
                if i in UsedWords:
                    words[1] += 3
            listOfWords.append(words)
    return listOfWords


def frequencies(text):
    textFrequencies = {
        "E": 0, "M": 0,
        "A": 0, "H": 0,
        "R": 0, "G": 0,
        "I": 0, "B": 0,
        "O": 0, "F": 0,
        "T": 0, "Y": 0,
        "N": 0, "W": 0,
        "S": 0, "K": 0,
        "L": 0, "V": 0,
        "C": 0, "X": 0,
        "U": 0, "Z": 0,
        "D": 0, "J": 0,
        "P": 0, "Q": 0
    }
    for chars in text:
        for letter in chars:
            char = ord(letter)
            if ord("z") >= char >= ord("a"):
                textFrequencies[letter.upper()] += 1
    print(textFrequencies["E"])
    new = ({k: v for k, v in sorted(textFrequencies.items(), key=lambda item: item[1])[::-1]})
    print(new)


translate = ""
file = open("Encrypted.txt", "r")
for item in file:
    translate += item.lower()
translate = translate.split(" ")
file.close()

#listOfWords = affine(translate)
#listOfWords = sorted(listOfWords, key=itemgetter(1))

frequencyAttempt = frequencies(translate)
print(frequencyAttempt)
'''
for i in listOfWords:
    for word in (i[0]):
        print(word, end=" ")
    print("\n")

print(listOfWords[-1][0])
if input("Save? ") == "yes":
    for i in listOfWords[-1][0]:
        UsedWords += i + " "
    print(UsedWords)
    file = open("UsedWords.txt", "w")
    file.write(UsedWords)
    file.close()
'''