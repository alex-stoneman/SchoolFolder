from operator import itemgetter

def english_frequency(jumbles):
    global  english
    for item in jumbles:
        points = 0
        current = item[0][:3]
        for letter in item[0]:
            try:
                points += english[current]
            except KeyError:
                points -= 500
            current = current[1:] + letter
        item.append(points)

    jumbles = sorted(jumbles, key=itemgetter(1))[::-1]
    print(jumbles[0][0])
    certainty = (jumbles[0][1] - jumbles[1][1]) // 10000
    if certainty > 99:
        print("100% certain")
    else:
        print(f"{certainty}% certain")


def columnar_recurr(keys, length, solutions, current, indexes, unused):
    if len(unused) != 1:
        for item in unused:
            current.append(item)
            new = (unused.copy())
            new.remove(item)
            solutions = columnar_recurr(keys, length, solutions, current, indexes, new)
            current.remove(item)
    else:
        current.append(unused[0])
        message = " "
        for item in keys:
            for index in current:
                try:
                    message += item[index]
                except AttributeError:
                    print(item)
        solutions.append([message])
        current.remove(unused[0])
        return solutions
    return solutions


def columnar(text):
    keys = []
    num = 5
    for x in range(len(text) // num):
        keys.append(text[x::len(text) // num])
    print(keys)
    solutions = []
    indexes = []
    for x in range(num):
        indexes.append(x)
    current = []
    unused = indexes[::]
    solutions = columnar_recurr(keys, num, solutions, current, indexes, unused)
    english_frequency(solutions)




encryptedMessage = ""
filename = "6a.txt"
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

print(len(message))
print(message[0])
print(message[295])
print(message[590])
columnar(message)