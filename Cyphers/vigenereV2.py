translate = ""
file = open("Encrypted.txt", "r")
for item in file:
    translate += item.lower()
file.close()
message = ""
for letter in translate:
    if ord("a") <= ord(letter) <= ord("z") or ord(letter) == 32:
        message += letter
message = message.split(" ")
def probability(possiblities):


def ceasar_shift(gibberish):
    possible_solutions = []
    for x in range(1,26):
        words = ""
        for letter in gibberish:
            char = ord(letter) + x
            if char > ord("z"):
                char -= 26
            words += chr(char)
        possible_solutions.append(words)
    probability(possible_solutions)


keys = []
for x in range(5):
    ceasar = ""
    for item in message:
        try:
            ceasar += item[x]
        except IndexError:
            pass
    print(ceasar)
    keys.append(ceasar)


