def read_in():
    file = open("encryptedMessage.txt", "r")
    text = file.readline()
    file.close()
    return text


message = read_in()
index = (len(message) - 1) // 4 + 7
rails = ord(message[index]) - 95
print(rails)