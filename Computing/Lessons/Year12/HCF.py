def HCF(a, b):
    while True:
        a %= b
        if a == 0:
            return b
        elif b % a == 0:
            return a
        else:
            a, b = b, a


while True:
    a = int(input("Enter: "))
    b = int(input("Enter: "))
    if a < b:
        a, b = b, a
    print(HCF(a, b), "\n")
