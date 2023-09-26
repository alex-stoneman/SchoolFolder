def fib(num):
    c = 1
    d = 1
    for x in range(num - 2):
        c, d = d, (c + d)
    return d

a = 1
b = 1
n = 2
chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    a, b = b, (a + b)
    n += 1
    a = int(str(a)[-9:])
    b = int(str(b)[-9:])
    check = True
    for char in chars:
        if char not in str(b):
            check = False

    if check:
        first = str(fib(n))[:9]
        print(n)
        print(first)
        print()
        for char in chars:
            if char not in first:
                check = False

    if check:
        print(fib(n))
        print(n)
        print("AAAAAAAAAAAAA\n" * 20)
        break

