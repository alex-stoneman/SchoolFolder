def to_roman(number):
    roman = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    final = ""
    while number != 0:
        for item in roman:
            digit = int(str(number)[0])
            if item <= number:
                final += roman[item]
                number -= item
                break
            elif digit == 4 and len(str(item)) <= len(str(number)):
                final += roman[item // 5] + roman[item]
                number -= item - item // 5
                break
            elif digit == 9 and len(str(item)) <= len(str(number)) + 1 and str(item)[0] != "5":
                final += roman[item // 10] + roman[item]
                number -= item - item // 10
                break
    return final


def from_roman(romanNumber):
    number = 0
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10,  "V": 5,  "I": 1}
    while len(romanNumber) != 0:
        try:
            if roman[romanNumber[0]] >= roman[romanNumber[1]]:
                number += roman[romanNumber[0]]
                romanNumber = romanNumber[1:]
            else:
                number += roman[romanNumber[1]] - roman[romanNumber[0]]
                romanNumber = romanNumber[2:]
        except IndexError:
            number += roman[romanNumber[0]]
            romanNumber = ""
    return number


while True:
    num = input("Enter roman numerals or a number less than 3000: ")
    try:
        if int(num) < 3001:
            print(to_roman(int(num)))
    except ValueError:
        correct = True
        for letter in num:
            if letter not in "IVXLCDM":
                correct = False
        if correct:
            givenNumber = from_roman(num)
            correctNumeral = to_roman(givenNumber)
            if num == correctNumeral:
                print(givenNumber)
            else:
                print(f"{num} is an invalid roman numeral")
