import csv
import matplotlib.pyplot as plt


def read_in(fileName):
    file = open(fileName, "r")
    csvReader = csv.reader(file)
    values = []
    for row in csvReader:
        values.append(row)
    file.close()
    return values


energyValues = []
massNumber = []
rows = read_in("bindingEnergy.csv")
for item in rows:
    massNumber.append(float(item[3]))
    p = 1.007825 * int(item[1])
    n = 1.008665 * (int(item[2]) - int(item[1]))
    massDefect = p + n - float(item[3])
    bindingEnergy = massDefect * 934.325
    bindingEnergyPerNucleon = bindingEnergy / int(item[2])
    energyValues.append(bindingEnergyPerNucleon)


plt.plot(massNumber, energyValues)
plt.plot(massNumber[25], energyValues[25], "ro", label="Fe")
plt.xlabel("Mass Number")
plt.ylabel("Binding Energy per Nucleon")
plt.title("The change in Binding Energy per Nucleon due to Mass number")
plt.xlim(0, 220)
plt.ylim(0, 10)
plt.legend()
plt.show()
