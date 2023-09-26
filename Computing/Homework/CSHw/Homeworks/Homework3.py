singleDigits = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                9: "nine"}
teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
         18: "eighteen", 19: "nineteen"}
doubleDigits = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
                9: "ninety"}


def double_digits(n):
    global singleDigits,doubleDigits,teens
    if 10 < n < 20:
        return teens[n]
    elif len(str(n)) == 2:
        first =  int(str(n)[0])
        second = int(str(n)[1])
        if second == 0:
            return doubleDigits[first]
        else:
            return f"{doubleDigits[first]} {singleDigits[second]}"
    else:
        return singleDigits[n]


def pence(p):
    p -= int(p)
    p = round(p*100)
    return double_digits(p)

def checks():
    global singleDigits,doubleDigits,teens
    num = float(input())
    if num >100:
        hundreds = int(str(num)[0])
        tens = int(float(str(num)[1:]))
        caps = singleDigits[hundreds][0].upper() + singleDigits[hundreds][1:]
        print(f"{caps} hundred", end="")
        if num % 100 != 0:
            print(f" and {double_digits(tens)} pounds", end="")
            if num - int(num) != 0:
                print(f" and {pence(num)} pence only")
            else:
                print(" only")
        else:
            print(" only")
    elif num > 1:
        tens = int(num)
        caps = double_digits(tens)[0].upper() + double_digits(tens)[1:]
        print(f"{caps} pounds", end="")
        if num - int(num) != 0:
            print(f" and {pence(num)} pence only")
        else:
            print(" only")
    else:
        pennies = pence(num)
        print(f"{pennies[0].upper()}{pennies[1:]} pence only")



while True:
    checks()