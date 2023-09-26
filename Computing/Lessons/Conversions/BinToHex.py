def check(number, baseFrom, baseTo, chars):
    for x in str(number):
        try:
            if int(x) > baseFrom:
                return False
        except ValueError:
            if x.upper() not in chars:
                return False
        if baseTo > 36 or baseFrom > 36 or baseTo < 2 or baseFrom < 2:
            return False
    return True


def convert(num, base, new):
    characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    try:
        if check(num, base, new, characters):
            total = 0
            n = len(str(num))
            for unit in str(num):
                total += characters.index(unit) * base ** (n-1)
                n -= 1
            # print(f"Base 10 = {total}")
            number = []
            numOfChars = 1
            while total >= new ** numOfChars:
                numOfChars += 1

            temp = numOfChars
            for x in range(temp):
                if total != 0:
                    current = total // (new ** (numOfChars-1))
                    number.append(characters[current])
                    total -= current * (new ** (numOfChars-1))
                    numOfChars -= 1
                else:
                    number.append("0")
            #print(f"Base {new} = ", end="")
            summary = ""
            for x in number:
                summary += str(x)
            # print("\n")
            return summary
        else:
            print("This doesn't work...\n")
    except ValueError:
        print("What?... What are you trying to say?\n")


while True:
    n = input("Input a number: ")
    b = int(input("What base is this in: "))
    o = int(input("What base do you want it in?"))
    convert(n, b, o)