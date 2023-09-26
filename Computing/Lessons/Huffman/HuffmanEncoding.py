def to_binary(number):
    numOfChars = 1
    while number >= 2 ** numOfChars:
        numOfChars += 1
    new = ""
    for x in range(numOfChars):
        current = number // (2 ** (numOfChars - 1))
        new += str(current)
        number -= current * 2 ** (numOfChars - 1)
        numOfChars -= 1
    if new == "0":
        return "00"
    elif new == "1":
        return "01"
    else:
        return new


def bubble_sort(unsorted):
    no_change = False
    while not no_change:
        previous = 0
        no_change = True
        for current in range(1, len(unsorted)):
            if unsorted[previous][0] > unsorted[current][0]:
                unsorted[previous], unsorted[current] = unsorted[current], unsorted[previous]
                no_change = False
            previous = current
    return unsorted

def go_thorough_list(searching, layer, finalLayer, letterFrequencies):
    letterFrequencies[searching[0][0]] = to_binary(2 ** (layer + 1) - 4)
    letterFrequencies[searching[0][1]] = to_binary(2 ** (layer + 1) - 3)
    if layer != finalLayer:
        go_thorough_list(searching[1], (layer + 1), finalLayer, letterFrequencies)
    else:
        for x in range(len(searching[1])):
            letterFrequencies[searching[1][x]] = to_binary(2 ** (layer + 1) - 2 + x)
    #return letterFrequencies


def letter_frequency(message):
    letterFrequencies = {}
    for letter in message:
        if letter in letterFrequencies:
            letterFrequencies[letter] += 1
        else:
            letterFrequencies[letter] = 1
    listOfFrequencies = []
    for item in letterFrequencies:
        listOfFrequencies.append([letterFrequencies[item], item])

    listOfFrequencies = bubble_sort(listOfFrequencies)[::-1]
    print(listOfFrequencies)
    pairs = []
    for x in range(len(listOfFrequencies)):
        if x % 2 == 0:
            pairs.append([listOfFrequencies[x][1]])
        else:
            pairs[-1].append(listOfFrequencies[x][1])

    layers = len(pairs)
    while len(pairs) >2:
        new = pairs[:-2]
        new.append([pairs[-2], pairs[-1]])
        pairs = new
    go_thorough_list(pairs, 1, (layers - 1), letterFrequencies)
    return  letterFrequencies



text = input(": ")
dictionary = letter_frequency(text)
print(dictionary)
huffman = ""
for char in text:
    huffman += dictionary[char]
print(huffman)


translate = ""
current = ""
for digit in huffman:
    current += digit
    for item in dictionary:
        if dictionary[item] == current:
            current = ""
            translate += item

print(translate)
regularSize = len(text) * 8
percent = ((regularSize - len(huffman)) * 100) // regularSize
print(f"Regular size = {regularSize} bits")
print(f"Huffman size = {len(huffman)} bits")
print(f"Percent space saved = {percent}%\n")
