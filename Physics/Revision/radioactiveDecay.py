import random
import matplotlib.pyplot as plt
import numpy
import math as maths

def some_rolls(currentNumberOfSides, remaining, check, labels):
    values = [remaining]
    while remaining > 0:
        current = [random.randint(1, currentNumberOfSides) for x in range(remaining)]
        count = 0
        for item in current:
            if item != currentNumberOfSides:
                count += 1
        remaining = count
        values.append(remaining)
    if labels:
        plt.plot(values, label="Dice Decay")
    else:
        plt.plot(values)
    if check:
        plt.show()


def many_rolls(numberOfSides, remaining):
    for currentNumberOfSides in range(2,numberOfSides):
        some_rolls(currentNumberOfSides, remaining, False, False)
    plt.show()


def radioActive(A, numberOfSides, interval, check, labels):
    values = [A]
    times = [0]
    remaining = A
    t = 0
    e = maths.e
    constant = 1 / numberOfSides
    while remaining > 0:
        t += interval
        times.append(t)
        current = A * (e ** (-constant * t))
        values.append(current)
        remaining = round(current)
    if labels:
        plt.plot(times, values, label="Exponential Decay")
    else:
        plt.plot(times, values)
    if check:
        plt.show()



sides = 1000
rolls = 1000
# many_rolls(10, 10000)
some_rolls(20, rolls, False, True)
radioActive(rolls, 20, 0.1, False, True)
plt.legend()
plt.show()