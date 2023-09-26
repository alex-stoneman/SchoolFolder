def read_in():
    encryptedMessage = ""
    filename = "7b.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())
    file.close()
    message = encryptedMessage.split(" ")
    return message

def caesar(plaintext, key):
    cypherText = ""
    for character in plaintext.lower():
        char = ord(character) - key
        if char < ord("a"):
            char += 26
        cypherText += chr(char)
    return cypherText


text = read_in()
print(text)
final = ""
for item in text:
    total = 0
    for x in range(len(item)):
        total += int(item[x]) * 2 ** (4 - x)
    final += chr(total + 65)

print(final)
words = ""
for x in range(len(final)):
    if x % 7 == 0:
        words += caesar(final[x], 19)
    elif x % 7 == 1:
        words += caesar(final[x], 17)
    elif x % 7 == 2:
        words += caesar(final[x], 8)
    elif x % 7 == 3:
        words += caesar(final[x], 13)
    elif x % 7 == 4:
        words += caesar(final[x], 8)
    elif x % 7 == 5:
        words += caesar(final[x], 19)
    else:
        words += caesar(final[x], 24)
print(words)