import csv
import random
import math as maths
import matplotlib.pyplot as plt

def read_in(fileName):
    file = open(fileName, "r")
    csvReader = csv.reader(file)
    values = []
    for row in csvReader:
        values.append(float(row[0]))
    file.close()
    return values


def variance(set):
    mean = sum(set) / len(set)
    total = 0
    for item in set:
        total += (item - mean) ** 2
    return total / (len(set) - 1)

def standard_deviation(set):
    var = variance(set)
    return maths.sqrt(var)

sample = []
rows = read_in("grapesMeanData.csv")

for x in range(160):
    value = random.choice(rows)
    sample.append(value)
    rows.remove(value)

print(min(sample))
print(max(sample))
print(sum(sample) / len(sample))
print(variance(sample))
print(standard_deviation(sample))
print()
print()
bins = round((max(sample) - min(sample)) / 10, 5)
categories = {0: [0]}
for item in sample:
    if item < bins:
        categories[0][0] += 1.0
for x in range(1, 9):
    categories[round(x * bins, 4)] = [0]
    for item in sample:
        if x * bins <= item < (x + 1) * bins:
            categories[round(x * bins, 4)][0] += 1.0
categories[round(9 * bins, 4)] = [0]
for item in sample:
    if item > 9 * bins:
        categories[round(9 * bins, 4)][0] += 1.0


for item in categories:
    categories[item].append(round(categories[item][0] / len(sample), 4))
    print(item, categories[item])

plt.hist(categories)
plt.show()