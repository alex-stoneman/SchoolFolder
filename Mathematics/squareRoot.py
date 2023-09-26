import copy
import math as maths

square = 62457 ** 2
print(square)
root = 0
length = len(str(square)) - 1
parity = 1 - ((length + 1) % 2)
current = square // (10 ** (length - parity))
count = 0
while True:
    count += 1
    if count ** 2 > current:
        count -= 1
        break

root += count
current = (current - count ** 2) * 100
current += (square // (10 ** (length - parity - 2))) % (10 ** 2)
count *= 2
for repetition in range((length - parity) // 2):
    previous = [0, 0, 0]
    check = True
    y = 0
    while check:
        count *= 10
        for x in range(1, 10):
            if (count + x) * x > current:
                check = False
                break
            else:
                previous = [count, x, y]
        y += 1
    current = (current - (previous[0] + previous[1]) * previous[1]) * 100
    current += (square // (10 ** (length - parity - 2 * (repetition + 2)))) % (10 ** 2)
    count = previous[0] * 10 ** previous[2] + previous[1]
    root *= 10 ** previous[2]
    root = root * 10 + previous[1]
    print(previous)
    print(count)
print(root)

