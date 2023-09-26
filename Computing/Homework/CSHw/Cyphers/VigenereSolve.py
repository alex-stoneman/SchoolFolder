def read_in():
    encryptedMessage = ""
    filename = "6b.txt"
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
    return message[::-1], english


def triples_frequency_analysis(solution):
    score = 0
    current = solution[:3]
    for letter in solution:
        if current in english:
            score += english[current]
        else:
            score -= 200
        current = current[1:] + letter
    if score > 400000:
        print(score, solution)


def caesar(plaintext, key):
    cypherText = ""
    for character in plaintext.lower():
        char = ord(character) + key
        if char > ord("z"):
            char -= 26
        cypherText += chr(char)
    return cypherText


def find_key(key, plaintext):
    if len(key) != 5:
        for x in range(26):
            key.append(x)
            key = find_key(key,plaintext)
            key.pop()
        return key

    else:

        current = ""
        temporary = []
        for x in range(5):
            temporary.append(caesar(plaintext[x], key[x]))
        for x in range(len(temporary[0])):
            for y in range(5):
                current += temporary[y][x]
        triples_frequency_analysis(current)
        return key


plain, english = read_in()
separate = []
for x in range(5):
    separate.append(plain[x::5])

jumbles = find_key([], separate)
