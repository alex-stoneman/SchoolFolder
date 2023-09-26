equation1, mod1 = (input("Equation 1: ").replace(" ", "")).split("=")
equation2, mod2 = (input("Equation 2: ").replace(" ", "")).split("=")
xLimit = int(input("Limit for x: "))
yLimit = int(input("Limit for y: "))

coefficientX1, coefficientY1 = int(equation1.split("+")[0][0]), int(equation1.split("+")[1][0])
coefficientX2, coefficientY2 = int(equation2.split("+")[0][0]), int(equation2.split("+")[1][0])
modResult1, modValue1 = int(mod1.split("mod")[0]), int(mod1.split("mod")[1])
modResult2, modValue2 = int(mod2.split("mod")[0]), int(mod2.split("mod")[1])

for x in range(xLimit):
    for y in range(yLimit):
        if  (coefficientX1 * x + coefficientY1 * y) % modValue1 ==modResult1:
            if (coefficientX2 * x + coefficientY2 * y) % modValue2 == modResult2:
                print(x, y)