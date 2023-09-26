import copy

class stack:
    def __init__(self, size, typeUsed):
        self.size = size
        self.front = -1
        self.items = [typeUsed for _ in range(size)]

    def push(self, item):
        if not self.full_stack():
            self.front += 1
            self.items[self.front] = item
        else:
            raise IndexError("Stack is full")

    def pop(self):
        if not self.empty_stack():
            self.front -= 1
            return self.items[self.front + 1]
        else:
            raise IndexError("Stack is empty")

    def empty_stack(self):
        if self.front == -1:
            return True
        else:
            return False

    def full_stack(self):
        if self.front == self.size:
            return True
        else:
            return False

    def peek(self):
        if not self.empty_stack():
            return self.items[self.front]
        else:
            raise IndexError("Stack is empty")

    def remove(self, index):
        if self.front < index:
            raise IndexError("Stack doesn't contain that many items")
        elif index < 0:
            raise IndexError("Index give must be positive")
        else:
            for x in range(index, self.front):
                if x < self.size - 1:
                    self.items[x] = self.items[x+1]
            self.front -= 1

    def display(self):
        print(self.items)

# Maze solving using the stack class
if __name__ == "__main__":
    def find_adjacent(pos, maz):
        adjacent = []
        for change in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            node = [pos[0] + change[0], pos[1] + change[1]]
            if 0 <= node[0] < len(maz) and 0 <= node[1] < len(maz[0]):
                if maz[node[0]][node[1]] == 1:
                    adjacent.append(node)
        return adjacent


    originalMaze = [
        [1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]]
    maze = copy.deepcopy(originalMaze)
    target = [2, 3]
    position = [0, 0]
    places = stack(100, list)
    places.push([0, 0])
    solved = False
    while not solved:
        check =[item for item in find_adjacent(places.peek(), maze)]
        if len(check) == 0:
            places.pop()
        else:
            for item in check:
                places.push(item)
                maze[item[0]][item[1]] = 0
                if item == target:
                    solved = True

    # places.display()

    currentOptions = [[2, 3]]
    current = [2, 3]
    path = []

    while current != [0, 0]:
        while True:
            temp = places.pop()
            if temp in currentOptions:
                current = temp
                break
        path.append(current)
        currentOptions = find_adjacent(temp, originalMaze)
    print(path[::-1])