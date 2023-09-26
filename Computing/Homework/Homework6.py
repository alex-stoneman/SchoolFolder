a = 1
b = 1
n = 2
chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    a, b = b, (a + b)
    n += 1
    first = str(b)[:9]
    last = str(b)[-9:]
    check = True
    for char in chars:
        if char not in first:
            check = False
    if check:
        print("First =")
        print(first)
        for char in chars:
            if char not in last:
                check = False
                print("Last = ")
                print(last)
    if check:
        print(n)
        break
