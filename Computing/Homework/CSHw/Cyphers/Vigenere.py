from operator import itemgetter
import math

def read_in():
    encryptedMessage = ""
    filename = "6b.txt"
    file = open(f"Challenges/{filename}", "r")
    for line in file:
        encryptedMessage += (line.lower())
    message = ""
    for character in encryptedMessage:
        if ord("a") <= ord(character) <= ord("z"):
            message += character
    file.close()
    return message[::-1]


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors


def main():
    message = read_in()
    current = "0" + message[:2]
    index = 2
    differences = {}
    for letter in message[2:]:
        current = current[1:] + letter
        diff = message.find(current, index, -1)
        while diff != -1:
            try:
                differences[diff - index - 1] += 1
            except KeyError:
                differences[diff - index - 1] = 1
            diff = message.find(current, diff + 1, -1)
        index += 1

    #print(differences)
    mostCommon = {}
    for item in differences:
        for factor in prime_factors(item):
            if factor < 26:
                try:
                    mostCommon[factor] += 1 * differences[item]
                except KeyError:
                    mostCommon[factor] = 1 * differences[item]

    print(mostCommon)
    print(len(message))
    n = 5
    give = []
    for x in range(len(message) // n + 1):
        print(message[x * n: (x + 1) * n])
        give.append(message[x * len(message) // n: (x +1) * len(message) // n])
    return give

main()
