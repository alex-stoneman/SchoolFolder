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


def triples_frequency_analysis(solution, n):
    solutions = []
    score = 0
    current = solution[:3]
    for letter in solution:
        if current in english:
            score += english[current]
        else:
            score -= 200
        current = current[1:] + letter
    if score > 100000 * n:
        solutions.append(solution)
    return solutions

def caesar(plaintext, key):
    cypherText = ""
    for character in plaintext.lower():
        char = ord(character) + key
        if char > ord("z"):
            char -= 26
        cypherText += chr(char)
    return cypherText


plain, english = read_in()
print(plain)
separate = []
for x in range(7):
    separate.append(plain[x::7])

'''
anotherList = []
for x in range(5):
    testing = []
    for y in range(26):
        testing.append(caesar(separate[x], y))
    full = []
    for item in testing:
        full
    testing = triples_frequency_analysis(testing, x)
'''
