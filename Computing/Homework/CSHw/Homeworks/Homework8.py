def base_converter(number, base):
    numOfChars = 1
    while number >= base ** numOfChars:
        numOfChars += 1
    new = ""
    for x in range(numOfChars):
        current = number // (base ** (numOfChars - 1))
        new += str(current)
        number -= current * base ** (numOfChars - 1)
        numOfChars -= 1
    return int(new)


while True:
    n = int(input("No. digits: "))
    b = int(input("Base = "))
    for x in range(10 ** (n - 1), 10 ** n):
        total = 0
        for digit in str(x):
            total += int(digit) ** n
        if base_converter(total, b) == x:
            print(x)
