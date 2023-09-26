import copy
import random
import math as maths
import pygame
xMax = 500
yMax = 500
DisplayXMax = 1000
numberOfNodes = 12
path = set()
pygame.init()
mainFont = pygame.font.Font('freesansbold.ttf', 16)
smallFont = pygame.font.Font('freesansbold.ttf', 12)

def generate_points_random():
    coords = []
    for i in range(numberOfNodes):
        while True:
            new = [random.randint(1, xMax), random.randint(1, yMax)]
            check = True
            for item in coords:
                if abs(item[0] ** 2 + item[1] ** 2 - new[0] ** 2 - new[1] ** 2) < 20000:
                    check = False
            if check:
                break
        coords.append(new)
    return coords


def generate_weights(positions):
    weights = [[-1 for x in range(len(positions))] for x in range(len(positions))]
    for current in range(len(positions)):
        distances = []
        count = 0
        item = positions[current]
        for next in positions:
            distance = maths.sqrt((next[0] - item[0]) ** 2 + (next[1] - item[1]) ** 2)
            if distance != 0:
                distances.append([distance, count])
                if len(distances) > 3:
                    largest = [0, -1]
                    for node in distances:
                        if node[0] > largest[0]:
                            largest = [node[0], node[1]]
                    distances.remove(largest)
            count += 1
        noConnect = random.randint(2, 4)
        for x in range(noConnect):
            chosen = random.choice(distances)
            value = random.randint(2, 10)
            weights[chosen[1]][current] = value
            weights[current][chosen[1]] = value
    return weights


def check_points(connections):
    nodes = []
    for x in range(10):
        nodes.append(set())
        nodes[x].add(x)
    for a in range(len(connections)):
        for b in range(a, len(connections[a])):
            try:
                if connections[a][b] != -1:
                    for c in range(len(nodes)):
                        first = nodes[c]
                        if a in first and b not in first:
                            for d in range(len(nodes)):
                                second = nodes[d]
                                if b in second:
                                    union = set.union(first, second)
                                    nodes.remove(first)
                                    nodes.remove(second)
                                    nodes.append(union)
                                    raise IndexError
            except IndexError:
                pass
    return len(nodes)


def find_working_graph():
    check = 0
    while check != 1:
        nodes = generate_points_random()
        weights = generate_weights(nodes)
        check = check_points(weights)
    return nodes, weights


def find_shortest_untaken(weights):
    shortest = -1
    position = [0, 0]
    for x in range(len(weights)):
        item = weights[x]
        for y in range(len(item)):
            value = item[y]
            if (value < shortest or shortest == -1) and value != -1:
                shortest = value
                position = [x, y]
    return position


def kruskal(weights):
    working = copy.deepcopy(weights)
    connections = [set() for x in range(numberOfNodes)]
    lines = []
    for x in range(numberOfNodes):
        connections[x].add(x)
    while len(connections) > 1:
        shortest = find_shortest_untaken(working)
        groups = []
        for x in range(2):
            count = 0
            for item in connections:
                if shortest[x] in item:
                    groups.append(count)
                else:
                    count += 1
        if groups[0] != groups[1]:
            union = connections[groups[0]].union(connections[groups[1]])
            connections.pop(min(groups))
            connections.pop(max(groups) - 1)
            connections.append(union)
            lines.append(shortest)
        else:
            working[shortest[0]][shortest[1]] = -1
    return lines


def solving_not_A_djangavardo(graph):
    priorityQueue = {}
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            minValue = min(x, y)
            maxValue = max(x, y)
            priorityQueue[[minValue, maxValue]] = [-1, ""]




nodes, weights = find_working_graph()
solving_not_A_djangavardo(weights)
screen = pygame.display.set_mode([DisplayXMax + 200, yMax + 100])
running = True
lines = []
while True:
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN or event.type == pygame.FINGERDOWN:
                    nodes, weights = find_working_graph()
                    lines = kruskal(weights)
                else:
                    screen.fill((0, 0, 0))
                    for node in nodes:
                        pygame.draw.circle(screen, (255, 0, 0), (node[0] + 50, node[1] + 50), 6)
                    for x in range(len(weights)):
                        connection = weights[x]
                        for y in range(len(connection)):
                            if connection[y] != -1:
                                first = [nodes[x][0] + 50, nodes[x][1] + 50]
                                second = [nodes[y][0] + 50, nodes[y][1] + 50]
                                pygame.draw.line(screen, (0, 255, 0), first, second, 2)
                                middle = [(second[0] + first[0]) // 2, (second[1] + first[1]) // 2]
                                write = smallFont.render(str(weights[x][y]), True, "White")
                                screen.blit(write, middle)

                    for node in nodes:
                        pygame.draw.circle(screen, (255, 0, 0), (node[0] + 650, node[1] + 50), 6)
                    for line in lines:
                        first = [nodes[line[0]][0] + 650, nodes[line[0]][1] + 50]
                        second = [nodes[line[1]][0] + 650, nodes[line[1]][1] + 50]
                        pygame.draw.line(screen, (0, 0, 255), first, second, 2)
                        middle = [(second[0] + first[0]) // 2, (second[1] + first[1]) // 2]
                        write = mainFont.render(str(weights[line[0]][line[1]]), True, "White")
                        screen.blit(write, middle)
                    pygame.display.flip()
    except KeyboardInterrupt:
        print("Closing...")
        break


