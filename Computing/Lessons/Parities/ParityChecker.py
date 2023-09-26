def generate_check_digit(text):
    total = 0
    for char in text:
        if char == "1":
            total += 1
    if total % 2 == 0:
        return "0"
    else:
        return "1"


def check_digit_checker(text):
    total = 0
    for char in text[:-1]:
        if char == "1":
            total += 1
    total %= 2
    if str(total) == text[-1]:
        print("yes")
    else:
        print("N0")


def check_seven():
    listOfBins = []
    file = open("Parity.txt", "r")
    for item in file:
        listOfBins.append(item[:-1])
    file.close()
    print(listOfBins)
    # Check the rows
    rows = ""
    for x in range(7):
        rows += generate_check_digit(listOfBins[x])
        listOfBins[x] += rows[-1]
    # Check the columns
    columns = ""
    for x in range(8):
        chars = ""
        for item in listOfBins:
            chars += item[x]
        columns += generate_check_digit(chars)
    print(rows)
    print(columns)
    return rows, columns

check_seven()
