translate = ""
file = open("Encrypted.txt", "r")
for item in file:
    translate += item.lower()
file.close()

words = ""
for x in range(len(translate)):
    if x % 5 == 0 and x != 0:
        words += f" {translate[x]}"
    else:
        words += translate[x]

print(words)