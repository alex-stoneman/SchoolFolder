def read_in():
    encryptedMessage = ""
    filename = "7adiff.txt"
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
    return message, english


message, common = read_in()
rails  = 1
length = len(message)
while True:
    rails += 1
    forwards = True
    solution = []
    nums = []
    start = length // (2 * rails - 2)
    for x in range(rails):
        if x == 0 or x == rails - 1:
            nums.append(start)
        else:
            nums.append(2 * start)
    if sum(nums) != length:
        order = []
        for x in range(rails):
            order.append(x)
        for x in order[:-1][::-1]:
            order.append(x)
        for x in range(length - sum(nums)):
            nums[order[x]] += 1
    total = 0
    previous = 0
    for item in nums:
        total += item
        solution.append(message[previous: total + 1])
        previous += item

    indexes = []
    count = 0
    final = ""
    for x in range(rails):
        indexes.append(0)
    for x in range(len(message)):
        final += solution[count][indexes[count]]
        indexes[count] += 1
        if forwards:
            if count == rails - 1:
                forwards = False
                count -= 1
            else:
                count += 1
        else:
            if count == 0:
                forwards = True
                count += 1
            else:
                count -= 1

    points = 0
    current = final[:3]
    for letter in final:
        try:
            points += common[current]
        except KeyError:
            points -= 500
        current = current[1:] + letter
    if points // length > 5000000 // len(message):
        print(final)
        break
    else:
        print(final)
        print(points)



