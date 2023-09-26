def factors(number):
    facts = []
    for x in range(2, number//2 + 1):
        while number % x == 0:
            number /= x
            facts.append(x)
    return facts


file = open("8a.txt", "r")
message = ""
for item in file:
    for letter in item.lower():
        if ord("a") <= ord(letter) <= ord("z"):
            message += letter
file.close()

print(message)
print(len(message))
print(factors(len(message)))
