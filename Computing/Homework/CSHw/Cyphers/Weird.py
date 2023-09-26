def read_in():
    encryptedMessage = ""
    filename = "7a.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())[:-1]
    file.close()
    message = encryptedMessage.replace(" ", "")
    return message



text = read_in()
print(text)
poly = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "j"],
    ["k", "l", "m", "n", "o"],
    ["p", "q", "r", "s", "t"],
    ["u", "v", "w", "x", "y"]
]

final = ""
for x in range(len(text) // 2):
    current = [int(text[2 * x]), int(text[2 * x + 1])]
    final += poly[current[0] - 1][current[1] - 1]
print(final)