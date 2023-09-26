import csv

def read_in(fileName):
    file = open(fileName, "r")
    csvReader = csv.reader(file)
    values = []
    for row in csvReader:
        values.append(row)
    file.close()
    return values


def write(filename, values):
    file = open(filename, "w")
    csvWriter = csv.writer(file)
    print(values)
    csvWriter.writerows(values)


data = read_in("PhysicsDatabase.csv")
data.append(["hello there"])
write("PhysicsDatabase.csv", data)