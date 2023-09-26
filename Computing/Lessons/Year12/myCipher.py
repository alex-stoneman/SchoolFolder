import random
import math
from operator import itemgetter


def affine(num, add, multiply):
    shifted = num * multiply + add
    while shifted > 26:
        shifted -= 26
    return shifted


def read_in():
    file = open("message.txt", "r")
    text = ""
    for line in file.readlines():
        text += line[:-1]
    file.close()
    message = ""
    for character in text.lower():
        if ord("a") <= ord(character) <= ord("z"):
            message += character
    while len(message) < 64:
        message += "j"
    return message


def indentify_order(word):
    order = []
    numbered = []
    for letter in word:
        order.append([letter, ord(letter)])
    order = sorted(order, key=itemgetter(1))
    for letter in word:
        numbered.append(order.index([letter, ord(letter)]))
    return numbered


def encrypt(seed, key, word):
    affines = [1, 3, 5, 7, 11, 15, 17, 19, 21, 23, 25]
    random.seed(int(seed))
    message = read_in()
    textSeed = ""
    firstKey = str(int(str(random.randint(1111, 9999) * random.randint(1111, 9999))[::-1]) + 1)
    secondKey = ""
    for number in firstKey:
        x = affines[int(number)]
        secondKey += str(affine(int(number), x * 5, x))

    vigenereMessage = ""
    for x in range(math.ceil(len(message))):
        try:
            shift = int(secondKey[x % len(secondKey)])
            vigenereMessage += chr(affine(ord(message[x]) - 96, shift, 1) + 96)
        except IndexError:
            pass

    for x in indentify_order(word):
        textSeed += chr(int(seed[x]) * 2 + 97)
    insertSeed = vigenereMessage[:2] + textSeed[0] + textSeed[1]
    insertSeed += vigenereMessage[2:4] + textSeed[2]
    insertSeed += vigenereMessage[4:8] + textSeed[3]
    insertSeed += vigenereMessage[8:16] + textSeed[4]
    insertSeed += vigenereMessage[16:32] + textSeed[5] + vigenereMessage[32:]

    rails = []
    for x in range(key):
        rails.append("")

    forward = True
    rail = 0
    for index in range(len(insertSeed)):
        rails[rail] += insertSeed[index]
        if rail == 0 and not forward:
            rail += 1
            forward = True
        elif rail == key - 1 and forward:
            rail -= 1
            forward = False
        elif forward:
            rail += 1
        else:
            rail -= 1

    railFence = ""
    for item in rails:
        railFence += item

    insert = len(railFence) // 4 + 7
    final = railFence[:insert] + chr(key + 95) + railFence[insert:]
    print(final)
    print()
    file = open("encryptedMessage.txt", "w")
    file.write(final)
    file.close

seed = ""
for x in range(6):
    seed += str(random.randint(0, 9))
key = random.randint(2, 16)
word = input("Enter a 6 letter word (the key): ")
print(key)
encrypt(seed, key, word)
