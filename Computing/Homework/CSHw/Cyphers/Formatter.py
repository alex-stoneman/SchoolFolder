from operator import itemgetter

def read_in():
    encryptedMessage = ""
    filename = "6b.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())
    message = ""
    for character in encryptedMessage:
        if ord("a") <= ord(character) <= ord("z") or ord(character) == 32:
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
    print(message)

read_in()