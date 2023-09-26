import random
import pygame
import time

mazeWidth = 20
mazeHeight = 20


def generate_nodes():
    square = max(mazeHeight, mazeWidth)
    nodes = [[[] for x in range(square)] for y in range(square)]
    # nodes = [[[] for x in range(mazeWidth)] for y in range(mazeHeight)]
    return nodes


def generate_connections(nodes):
    included = [[0, 0]]
    startTime = time.perf_counter_ns()
    while len(included) < mazeHeight * mazeWidth:
        possible = []
        for item in included:
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                currentX = item[0]
                currentY = item[1]
                newX = currentX + x
                newY = currentY + y
                returnList = [newX, newY]
                if -1 < newX < mazeWidth and -1 < newY < mazeHeight:
                    if returnList not in nodes[currentX][currentY]:
                        if [item, returnList] not in possible:
                            if returnList not in included:
                                possible.append([item, returnList])
        choice = random.choice(possible)
        newNode = choice[1]
        included.append(newNode)
        nodes[choice[0][0]][choice[0][1]].append(newNode)
        nodes[newNode[0]][newNode[1]].append(choice[0])
    endTime = time.perf_counter_ns()
    print(nodes)
    print((endTime - startTime) / (10 ** 9))
    return nodes



boxSideLength = min(800 // mazeHeight, 1350 // mazeWidth)
boxes = generate_nodes()
connections = generate_connections(boxes)
pygame.init()
screen = pygame.display.set_mode([boxSideLength * mazeWidth + 2, boxSideLength * mazeHeight + 2])
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
            pygame.draw.rect(screen, (0, 255, 0), (((mazeWidth -1) * boxSideLength + 1, (mazeHeight -1) * boxSideLength + 1), (boxSideLength -1, boxSideLength - 1)))
            for x in range(mazeWidth):
                for y in range(mazeHeight):
                    for xDiff in [-1, 0, 1]:
                        for yDiff in [-1, 0, 1]:
                            if abs(xDiff) != abs(yDiff):
                                if [x + xDiff, y + yDiff] not in connections[x][y]:
                                    if xDiff == 0:
                                        start = (x * boxSideLength, (boxSideLength // 2) + y * boxSideLength + yDiff * (boxSideLength // 2))
                                        end = (boxSideLength + x * boxSideLength, (boxSideLength // 2) + y * boxSideLength + yDiff * (boxSideLength // 2))
                                    else:
                                        start = ((boxSideLength // 2) + x * boxSideLength + xDiff * (boxSideLength // 2),y * boxSideLength)
                                        end = ((boxSideLength // 2) + x * boxSideLength + xDiff * (boxSideLength // 2), boxSideLength + y * boxSideLength)
                                    pygame.draw.line(screen, (0, 0, 255), start, end, 2)
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

