from operator import itemgetter

def affine(text, encrypt, multiply, add):
    if encrypt:
        encrypted = ""
        for letter in text:
            char = ord(letter) - 97 - add
            while char % multiply != 0 or char < 0:
                char += 26
            char //= multiply
            encrypted += chr(char + 97)
        return encrypted
    else:
        listOfWords = []
        for x in [1, 3, 5, 11, 15, 17, 19 ,21, 23, 25]:
            for y in range(26):
                decrypted = ""
                for letter in text:
                    char = ord(letter) - 97
                    char = char * x + y
                    while char > 25:
                        char -= 26
                    decrypted += chr(char + 97)
                listOfWords.append([decrypted])
        return listOfWords


def read_in():
    encryptedMessage = ""
    filename = "2b.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())
    message = ""
    for character in encryptedMessage:
        if ord("a") <= ord(character) <= ord("z"):
            message += character
    file.close()
    english = {}
    file = open("war_and_peace.txt", "r")
    war = file.readline()
    current = war[:3]
    for letter in war:
        try:
            english[current] += 1
        except KeyError:
            english[current] = 1
        current = current[1:] + letter
    return message, english


def english_frequency(jumbles):
    for item in jumbles:
        points = 0
        current = item[0][:3]
        for letter in item[0]:
            try:
                points += englishCommon[current]
            except KeyError:
                points -= 500
            current = current[1:] + letter
        item.append(points)

    jumbles = sorted(jumbles, key=itemgetter(1))[::-1]
    print(jumbles[0])
    certainty = (jumbles[0][1] - jumbles[1][1]) // 10000
    if certainty > 99:
        print("100% certain")
    else:
        print(f"{certainty}% certain")


def letter_frequency(message):
    letterFrequencies = {
        "e": [11.1607, ["e", 0]], "a": [8.4866, ["a", 0]], "r":[7.5809, ["r", 0]], "i": [7.5448, ["i", 0]],
        "o": [7.1635, ["o", 0]], "t": [6.9509, ["t", 0]], "n":[6.6544, ["n", 0]], "s": [5.7351, ["s", 0]],
        "l": [5.4893, ["l", 0]], "c": [4.5388, ["c", 0]], "u":[3.6308, ["u", 0]], "d": [3.3844, ["d", 0]],
        "p": [3.1671, ["p", 0]], "m": [3.0129, ["m", 0]], "h":[3.0034, ["h", 0]], "g": [2.4705, ["g", 0]],
        "b": [2.0720, ["b", 0]], "f": [1.8121, ["f", 0]], "y":[1.7779, ["y", 0]], "w": [1.2899, ["w", 0]],
        "k": [1.1016, ["k", 0]], "v": [1.0074, ["v", 0]], "x":[0.2902, ["x", 0]], "z": [0.2722, ["z", 0]],
        "j": [0.1965, ["j", 0]], "q": [0.1962, ["q", 0]]
    }
    error = 0
    for item in letterFrequencies:
        current = letterFrequencies[item]
        current[1][1] = message.count(item) / len(message) * 100
        error += (current[0] - current[1][1]) ** 2
    print(letterFrequencies)
    print(error)

    for item in letterFrequencies:
        old = letterFrequencies[item]
        for otherItem in letterFrequencies:
            new = letterFrequencies[otherItem]
            originalError = (old[0] - old[1][1]) ** 2
            newError = (old[0] - new[1][1]) ** 2
            if newError < originalError:
                error = error - originalError + newError
                old[1], new[1] = new[1], old[1]
            decrypted = ""
            for letter in message:
                for item in letterFrequencies:
                    if letterFrequencies[item][1][0] == letter:
                        decrypted += item
            print(letterFrequencies)
            print(decrypted)

message, englishCommon = read_in()
#final = affine(message, False, 0, 0)
#english_frequency(final)
letter_frequency(message)