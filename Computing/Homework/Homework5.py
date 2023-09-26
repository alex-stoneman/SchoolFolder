def boxes(r, c):
    max = len(str(r*c))
    sides = "-" * max + "+"
    for x in range(r):
        print("+" + sides * c + "\n|", end="")
        for y in range(1, c + 1):
            n = x * c + y
            print(" " * (max - len(str(n))) + f"{n}|", end="")
        print()
    print("+" + sides * c)


while True:
    rows = int(input("Input rows: "))
    columns = int(input("Input columns: "))
    boxes(rows, columns)
    print("\n" * 5)
