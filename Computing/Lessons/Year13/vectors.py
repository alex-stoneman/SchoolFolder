class vector:
    def __init__(self, values):
        self.values = values
        self.order = len(values)

    def __str__(self):
        img = ""
        longest = max(len(str(item)) for item in self.values)
        for item in self.values:
            img += f"|{str(item).rjust(longest)}|\n"
        return img

    def __repr__(self):
        return str(self.values)

    def __add__(self, other):
        if self.order == other.order:
            result = []
            for x in range(self.order):
                result.append(self.values[x] + eval(str(other))[x])
            return vector(result)
        else:
            raise IndexError

    def __eq__(self, other):
        if self.order == other.order:
            for x in range(self.order):
                self.values[x] = eval(str(other))[x]

    def __sub__(self, other):
        new = [-1 * item for item in eval(str(other))]
        self.__add__(vector(new))

    def __mul__(self, scalar):
        result = []
        for item in self.values:
            result.append(scalar * item)
        return vector(result)


a = vector([1, 3, 7])
print(a)
print(eval(a.__repr__())[2])