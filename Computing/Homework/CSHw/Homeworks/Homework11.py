def HCF(a, b):
    a %= b
    if a == 0:
        return b
    elif b % a == 0:
        return a
    else:
        return 1


while True:
    a = int(input("Enter: "))
    b = int(input("Enter: "))
    if a < b:
        a, b = b, a
    print(HCF(a, b), "\n")