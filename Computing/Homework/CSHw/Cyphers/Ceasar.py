from operator import itemgetter

def affine(text):
    listOfWords = []
    for x in [1, 3, 5, 11, 15, 17, 19 ,21, 23, 25]:
        for y in range(26):
            decrypted = ""
            for letter in text:
                char = ord(letter) - 97
                char = char * x + y
                while char > 25:
                    char -= 26
                decrypted += chr(char + 97)
            listOfWords.append([decrypted])
    return listOfWords

def read_in():
    encryptedMessage = ""
    filename = "7adiff.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())[:-1]
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
    return encryptedMessage, english


def english_frequency(problems):
    for problem in problems:
        points = 0
        current = problem[0][:3]
        for letter in problem[0]:
            try:
                points += common[current]
            except KeyError:
                points -= 500
            current = current[1:] + letter
        problem.append(points)

    problems = sorted(problems, key=itemgetter(1))[::-1]
    print(problems[0])
    certainty = (problems[0][1] - problems[1][1]) // 10000
    if certainty > 99:
        print("100% certain")
    else:
        print(f"{certainty}% certain")


print("H")
translate, common = read_in()
print(translate)
solutions = affine(translate)
print(solutions)
english_frequency(solutions)