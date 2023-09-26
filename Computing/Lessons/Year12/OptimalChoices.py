import random
options = {
    1: [0, 10],
    2: [0, 10],
    3: [0, 10],
    4: [0, 10],
    5: [0, 10],
    6: [0, 10],
    7: [0, 10],
    8: [0, 10],
    9: [0, 10],
    10: [0, 10]
}
choices = []
for x in range(100):
    a = random.randint(1, 10)
    b = a
    while b == a:
        b = random.randint(1, 10)
    c = b
    while c == b or c == a:
        c = random.randint(1, 10)
    choices.append([a, b, c])
print(choices)
points = [0, 0, 0]
for dunno in range(10):
    for something in range(3):
        for item in options:
            options[item][0] = 0
        for item in choices:
            options[item[something]][0] += 1
        print(options)

        for item in options:
            if options[item][0] <= options[item][1]:
                personCount = -1
                new = []
                for person in choices:
                    if person[something] == item:
                        options[item][0] -= 1
                        options[item][1] -= 1
                        points[something] += 1
                    else:
                        new.append(person)
                choices = new

        print()
        print(choices)
        print(options)
        print()

print(points)