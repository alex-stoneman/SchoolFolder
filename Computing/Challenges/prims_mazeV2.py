import copy
import random
import time

import pygame

mazeWidth = 100
mazeHeight = 100

def solve(nodes):
    solution = copy.deepcopy(nodes)
    action = True
    while action:
        action = False
        for y in range(mazeHeight):
            for x in range(mazeWidth):
                if len(solution[y][x]) == 1 and [y, x] != [0, 0] and [y, x] != [mazeHeight, mazeWidth]:
                    action = True
                    try:
                        for item in solution[y][x]:
                            solution[item[0]][item[1]].remove([y, x])
                    except IndexError:
                        pass
                    solution[y][x] = []
        print(solution)
    print(solution)
    final = [[0, 0]]
    new = [0, 0]
    while new != [mazeHeight, mazeWidth]:
        new = solution[new[0]][new[1]]
        final.append(new)
        print(final)
    return final


def generate_nodes():
    square = max(mazeHeight, mazeWidth)
    nodes = [[[] for x in range(square)] for y in range(square)]
    return nodes


def generate_connections(nodes):
    included = [[0, 0]]
    startTime = time.perf_counter_ns()
    possible = [[0, 1], [1, 0]]
    while len(included) < mazeHeight * mazeWidth:
        first = random.choice(possible)
        included.append(first)
        possible.remove(first)
        secondChoices = []
        for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            new = [first[0] + x, first[1] + y]
            if new not in possible and 0 <= new[0] < mazeWidth and 0 <= new[1] < mazeHeight:
                if new not in included:
                    possible.append(new)
                else:
                    secondChoices.append(new)
        second = random.choice(secondChoices)
        nodes[first[0]][first[1]].append(second)
        nodes[second[0]][second[1]].append(first)
    endTime = time.perf_counter_ns()
    print((endTime - startTime) / (10 ** 9))
    return nodes



boxSideLength = min(800 // mazeHeight, 1350 // mazeWidth)
if mazeWidth * mazeHeight > 30000:
    lineWidth = 1
else:
    lineWidth = 2
boxes = generate_nodes()
connections = generate_connections(boxes)
#solution = solve(connections)
#print(solution)
pygame.init()
screen = pygame.display.set_mode([boxSideLength * mazeWidth + lineWidth, boxSideLength * mazeHeight + lineWidth], pygame.RESIZABLE)
running = True
lines = []
while True:
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill([0, 0, 0])
            pygame.draw.rect(screen, (0, 255, 0), ((1, 1), (boxSideLength -1, boxSideLength - 1)))
            pygame.draw.rect(screen, (0, 255, 0), (((mazeWidth -1) * boxSideLength + lineWidth, (mazeHeight -1) * boxSideLength + lineWidth), (boxSideLength -1, boxSideLength - 1)))
            for x in range(mazeWidth):
                for y in range(mazeHeight):
                    for xDiff, yDiff in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        if [x + xDiff, y + yDiff] not in connections[x][y]:
                            if xDiff == 0:
                                start = (x * boxSideLength, (boxSideLength // 2) + y * boxSideLength + yDiff * (boxSideLength // 2))
                                end = (boxSideLength + x * boxSideLength, (boxSideLength // 2) + y * boxSideLength + yDiff * (boxSideLength // 2))
                            else:
                                start = ((boxSideLength // 2) + x * boxSideLength + xDiff * (boxSideLength // 2),y * boxSideLength)
                                end = ((boxSideLength // 2) + x * boxSideLength + xDiff * (boxSideLength // 2), boxSideLength + y * boxSideLength)
                            pygame.draw.line(screen, (0, 0, 255), start, end, lineWidth)
                    '''
                    for item in connections[x][y]:
                        xCoord = 30 + (item[0]) * 40
                        yCoord = 30 + (item[1]) * 40
                        pygame.draw.line(screen, (0, 0, 255), coords, (xCoord, yCoord), 4)
                    '''
            pygame.display.flip()
    except KeyboardInterrupt:
        print("Closing...")
        break

