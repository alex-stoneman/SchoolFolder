import random, math

def input_coords(nodes):
    coords = []
    for i in range(nodes):
        coords.append(int(input("Input x coord: "), int(input("Input y coord:"))))
    return coords


def node_coords(x,y,nodes):
    coords = []
    for i in range(nodes):
        coords.append([random.randint(1,x),random.randint(1,y)])
    return coords

def dict_of_distances(coords):
    dictionary = {}
    nodeCount = -1
    for i in coords:
        nodeCount += 1
        dictionary[nodeCount + 1] = []
        inLoopNodeCount = -1
        for i in coords:
            inLoopNodeCount += 1
            xDistance = abs(coords[nodeCount][0] - coords[inLoopNodeCount][0])
            yDistance = abs(coords[nodeCount][1] - coords[inLoopNodeCount][1])
            distance = math.sqrt((xDistance ** 2) + (yDistance ** 2))
            dictionary[nodeCount + 1].append(round(distance,4))
    return dictionary


def not_mapping(xRan,yRan, nodes):
    angle = 0
    coords = []
    dictionary = {}
    for x in range(nodes):
        xVal = xRan + xRan * math.sin(angle)
        yVal = yRan + yRan * math.cos(angle)
        coords.append((xVal, yVal))
        angle += math.pi * 2 / nodes
        #print(angle)
        #print(math.sin(angle))
        #print(math.cos(angle))

    for x in range(1, nodes + 1):
        #print(dictionary)
        if x == 1:
            dictionary[1] = [0]
            for y in range(nodes - 1):
                dictionary[1].append(random.randint(1,5000))
        else:
            dictionary[x] = []
            for y in range(1, x):
                dictionary[x].append(dictionary[y][x-1])
            dictionary[x].append(0)
            for y in range(nodes - x):
                dictionary[x].append(random.randint(1, 5000))
    return coords, dictionary


xRange = 300
yRange = 300
#nodes = 3
def run():
    nodes = int(input("Enter the number of nodes: "))
    coords = node_coords(xRange,yRange,nodes)
    distances = dict_of_distances(coords)
    return coords, distances

def run_other():
    nodes = int(input("Enter the number of nodes: "))
    coords, distances = not_mapping(150, 150, nodes)
    return coords, distances

def run_stored():
    pass