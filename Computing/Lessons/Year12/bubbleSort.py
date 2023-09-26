def bubble(myItems):
    changes = True
    while changes:
        changes = False
        previous = 0
        for item in range(len(myItems)):
            if myItems[previous] > myItems[item]:
                myItems[previous], myItems[item] = myItems[item], myItems[previous]
                changes = True
            previous = item
    return myItems



myItems = [1, 8, 3, 94, 2, 5]
print(bubble(myItems))

wordsInfile = ""
file = open("Textfile.txt", "r")
for line in file:
    wordsInfile += line
