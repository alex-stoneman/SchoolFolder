from operator import itemgetter

def affine(text, encrypt, multiply, add):
    #text = text.remove(" ")
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
    filename = "5b.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())
    message = ""
    for character in encryptedMessage:
        if ord("a") <= ord(character) <= ord("z") or ord(character) == 32 or character == "/":
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

def morse_translator(message):
    morse = ["ad", "daaa", "dada", "daa", "a", "aada", "dda", "aaaa", "aa", "addd", "dad", "adaa", "dd", "da", "ddd", "adda", "ddad", "ada", "aaa", "d", "aad", "aaad", "add", "daad", "dadd", "ddaa"]
    new = []
    message = message.split("/")
    for item in message:
        new.append(item.split())

    translate = ""
    for word in new:
        complete = ""
        for letter in word:
            num = morse.index(letter)
            complete += chr(num + 97)
        translate += complete
    return translate

#do Stuff
message, englishCommon = read_in()
morseText = morse_translator(message)

final = affine(morseText, False, 0, 0)
english_frequency(final)