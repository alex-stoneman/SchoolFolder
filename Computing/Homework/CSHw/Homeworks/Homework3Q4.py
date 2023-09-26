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
            return f"{doubleDigits[first]}{singleDigits[second]}"
    else:
        return singleDigits[n]

def checks(num):
    global singleDigits,doubleDigits,teens

    if num > 99:
        hundreds = int(str(num)[0])
        tens = int(str(num)[1:])
        out = f"{singleDigits[hundreds]}hundred"
        if num % 100 != 0:
            out += f"and{double_digits(tens)}"
        return out

    else:
        return double_digits(num)

total = ""
for x in range(1,1000):
    total += checks(x)

print(len(total)+11)
