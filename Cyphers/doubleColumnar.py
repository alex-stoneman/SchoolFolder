encrypted = ""
file = open("6a.txt", "r")
for line in file:
    for letter in line:
        if ord("A") <= ord(letter) <= ord("Z"):
            encrypted += letter.lower()
n = 7
keys = []
for x in range(len(encrypted) // 7):
    keys.append([encrypted[x * 7: (x + 1) * 7]])

print(keys)