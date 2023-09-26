import random


class queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.items = [None for _ in range(size)]
        self.numberOfItems = 0

    def enqueue(self, item):
        if self.numberOfItems != self.size:
            self.items[self.rear] = item
            self.rear += 1
            self.numberOfItems += 1
            if self.rear == self.size:
                self.rear = 0
        else:
            raise MemoryError

    def dequeue(self):
        if self.numberOfItems != 0:
            value = self.items[self.front]
            self.front += 1
            if self.front == self.size:
                self.front = 0
            return value
        else:
            raise IndexError

    def __str__(self):
        out = "["
        if self.front < self.rear:
           for item in self.items[self.front:self.rear]:
               out += f"{item}, "
        else:
            for item in self.items[self.front:]:
                out += "[" + f"{item}, "
            for item in self.items[:self.rear]:
                out += "[" + f"{item}, "
        out = out[:-2]
        out += "]"
        return out

mine = queue(50)
for x in range(30):
    mine.enqueue(random.randint(4, 50))
print(mine)