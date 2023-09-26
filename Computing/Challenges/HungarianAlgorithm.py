import random


class Matrix():
    def __init__(self, listOfLists=None, rowLength = 10, columnLength = 10):
        if listOfLists is None:
            listOfLists = []
        self.store = listOfLists
        self.rowLength = rowLength
        self.columnLength = columnLength


    def randomise(self, randomRange = 100):
        self.store = []
        for x in range(self.rowLength):
            self.store.append([])
            for y in range(self.columnLength):
                self.store[-1].append(random.randint(1, randomRange))


    def get_row(self, row):
        return self.store[row]


    def get_column(self, column):
        values = []
        for row in self.store:
            values.append(row[column])
        return values

    def change_row(self, row, change):
        for x in range(self.rowLength):
            self.store[row][x] += change

    def change_column(self, column, change):
        for y in range(self.columnLength):
            self.store[y][column] += change

    def find_zeros(self):
        zeros = []
        for row in range(self.columnLength):
            for column in range(self.rowLength):
                if self.store[row][column] == 0:
                    zeros.append((row, column))
        return zeros

    def find_least_lines(self):
        horizontalLines = []
        verticalLines = []
        zeros = self.find_zeros()
        horizontalTests = set()
        verticalTests = set()
        for item in zeros:
            horizontalTests.add(item[0])
            verticalTests.add(item[1])
        lines = 1
        while True:
            pass




columns = 4
rows = 4
myMatrix = Matrix([], rows, columns)
myMatrix.randomise()


for row in range(rows):
    smallest = -min(myMatrix.get_row(row))
    myMatrix.change_row(row, smallest)

for column in range(columns):
    smallest = -min(myMatrix.get_column(column))
    myMatrix.change_column(column, smallest)

for x in range(rows):
    print(myMatrix.get_row(x))
