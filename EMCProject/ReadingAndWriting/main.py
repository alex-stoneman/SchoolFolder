from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt


def read_file(filename):
    file = open(filename, "r")
    happiness = []
    for line in file:
        line = line.split(",")
        happiness.append(line[:-2])
    return happiness


happiness = {}
for x in range(2015, 2018):
    happiness[x] = read_file(f"World Happiness {x}.csv")

count = 0
for measure in happiness[2015][0]:
    count += 1
    print(f"{count}: {measure}")
print("")

while True:
    first = int(input("First measure: "))
    second = int(input("Second measure: "))
    if 1 <= first <= 10 and 1 <= second <= 10 and first != second:
        break
    else:
        print(" ")


host = host_subplot(111, axes_class=axisartist.Axes)
#plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()


p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")

host.set_xlim(0, 2)
host.set_ylim(0, 2)
par1.set_ylim(0, 4)
par2.set_ylim(1, 65)

host.set_xlabel("Distance")
host.set_ylabel("Density")

host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.show()