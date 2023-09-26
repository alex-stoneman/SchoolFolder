class OrderedBinaryTree:
    data = []
    treeType = "unknown"
    def __init__(self, values=None):
        if values is not None:
            self.__add__(values)

    def __add__(self, other):
        if type(other) == list:
            for item in other:
                self.__add__(item)

        elif type(other) == self.treeType or self.treeType == "unknown":
            self.place_in_data(self.value(other), 0)
        else:
            try:
                self.place_in_data(self.treeType(other), 0)
            except:
                print(f"Value {other} of {type(other)} was of the "
                  f"incorrect data type for this binary tree")

    def __copy__(self):
        info = [item[1] for item in self.data]
        return OrderedBinaryTree(info)

    def value(self, v):
        if self.treeType is str:
            return ord(v)
        elif self.treeType is int:
            return int(v)
        elif self.treeType is float:
            return float(v)
        elif self.treeType == "unknown":
            self.treeType = type(v)
            return self.value(v)
        else:
            raise Exception(f"You are attempting to use the unsupported {type(v)}")


    def place_in_data(self, v, index):
        if v is not None:
            try:
                node = self.data[index]
                if v < node[1]:
                    check = 2 # left position
                else:
                    check = 3 # right position
                if node[check] is None:
                    newIndex = len(self.data)
                    node[check] = newIndex
                    self.data.append([newIndex, v, None, None])
                else:
                    self.place_in_data(v, node[check])

            except IndexError:
                self.data.append([0, v, None, None]) # [Index, value, Index of LC, Index of RC]
            except TypeError:
                print(self.data)

    def display(self):
        print(self.data)

    def in_order_traversal(self, index=0, orderedList=None):
        if orderedList is None:
            orderedList = []
        leftChild = self.data[index][2]
        if leftChild is not None:
            orderedList = self.in_order_traversal(leftChild, orderedList)
        orderedList.append(self.data[index][1])
        rightChild = self.data[index][3]
        if rightChild is not None:
            orderedList = self.in_order_traversal(rightChild, orderedList)
        return orderedList


    def pre_order_traversal(self, index=0, orderedList=None):
        if orderedList is None:
            orderedList = []
        orderedList.append(self.data[index][1])
        leftChild = self.data[index][2]
        if leftChild is not None:
            orderedList = self.pre_order_traversal(leftChild, orderedList)
        rightChild = self.data[index][3]
        if rightChild is not None:
            orderedList = self.pre_order_traversal(rightChild, orderedList)
        return orderedList

    def post_order_traversal(self, index=0, orderedList=None):
        if orderedList is None:
            orderedList = []
        leftChild = self.data[index][2]
        if leftChild is not None:
            orderedList = self.pre_order_traversal(leftChild, orderedList)
        rightChild = self.data[index][3]
        if rightChild is not None:
            orderedList = self.pre_order_traversal(rightChild, orderedList)
        orderedList.append(self.data[index][1])
        return orderedList

    def ordered_list(self):
        return self.in_order_traversal(0, [])

    def search(self, value, index=0):
        if self.data[index][1] == value:
            return True
        else:
            leftChild = self.data[index][2]
            if leftChild is not None:
                if self.search(value, leftChild):
                    return True
            rightChild = self.data[index][3]
            if rightChild is not None:
                if self.search(value, rightChild):
                    return True
        return False

    def find_layers(self, layeredList=None, currentLayer = 0):
        if layeredList is None:
            layeredList = [[self.data[0]], []]
        else:
            layeredList.append([])
        finalLayer = True
        for item in layeredList[currentLayer]:
            for x in [2, 3]:
                if item[x] is not None:
                    layeredList[currentLayer + 1].append(self.data[item[x]])
                    finalLayer = False
        if not finalLayer:
            return self.find_layers(layeredList, currentLayer + 1)
        else:
            return layeredList[:-1]







tree = OrderedBinaryTree([2.5, 6.2, 9.1, 4, 3, 7, 1])
tree + "e"
print(tree.ordered_list())
print(tree.pre_order_traversal())
print
print(tree.search(10))
print(tree.data)
print(tree.find_layers())
# layers = tree.find_layers()
# for layer in layers:
#     print(" ".join([str(val[1]) for val in layer]))
# display = ["" for _ in range(len(layers))]
# print("           _______ 1 _______\n"
#       "          /                  \ \n"
#       "     ___ 2 ___             __ 3 __\n"
#       "    /         \           /       \ \n"
#       "  40           5         6         7 \n"
#       " /   \       /   \     /   \     /   \ \n"
#       "8     9    10     1   2     3   4     5")
