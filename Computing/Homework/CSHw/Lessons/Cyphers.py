def caesar(plaintext, key, direction):
    cypherText = ""
    for character in plaintext.lower():
        if ord("a") <= ord(character) <= ord("z"):
            char = ord(character) + key * direction
            if char > ord("z"):
                char -= 26
            if char < ord("a"):
                char += 26
            cypherText += chr(char)
        else:
            cypherText += character
    return cypherText


while True:
    encode = input("Do you want to encrypt or decrypt: ")
    if encode.lower() == "encrypt":
        encode = 1
    else:
        encode = -1
    message = input("Enter your message: ")
    key = int(input("Enter your key: "))
    print(caesar(message, key, encode), "\n")