from operator import itemgetter
sybList = []
for x in range(32, 127):
    sybList.append([chr(x), 0])
for char in input(": "):
    sybList[ord(char)-32][1] += 1

sybList = sorted(sybList, key=itemgetter(1))[::-1]
print(sybList)