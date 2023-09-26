morse = ["ad", "daaa", "dada", "daa", "a", "aada", "dda", "aaaa", "aa", "addd", "dad", "adaa", "dd", "da", "ddd", "adda", "ddad", "ada", "aaa", "d", "aad", "aaad", "add", "daad", "dadd", "ddaa"]
file = open(f"Challenges/5b.txt", "r")
encryptedMessage = ""
for line in file:
    encryptedMessage += (line.lower())
message = ""
for character in encryptedMessage:
    if ord("a") <= ord(character) <= ord("z") or ord(character) == 32:
        message += character
message = message.split(" ")
final = ""
for item in message:
    print(morse.index(item))
    final += chr(morse.index(item) + ord("a"))
print(final)