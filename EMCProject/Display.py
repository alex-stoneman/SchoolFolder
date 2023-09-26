import pygame
import CreateNodes
import Heuristics
import math
from time import sleep
# A function to adjust the coords So that they are centred on the screen
# Inputs the coords,


def adjust_to_centre(coordinates, index, xDifference, yDifference):
    return [coordinates[index][0] + xDifference, coordinates[index][1] + yDifference]


# Determine if the wanted set of nodes is distance based or path value bases
def run_for_distance():
    if input("Distance or Value: ").upper() == "VALUE":
        value = True
        # coordinates, distances = CreateNodes.run_other()
        coordinates, distances = CreateNodes.run_stored()
    else:
        value = False
        coordinates, distances = CreateNodes.run()

    # find the best routes, and paths taken by the different Heuristics
    if len(coordinates) < 15:
        bruteSolutions, bruteShortest = Heuristics.brute_force(distances)
        #print(bruteSolutions)

    else:
        bruteSolutions = [[0]]
        bruteShortest = ["Na", [0]]
    nearestSolutions, nearestShortest = Heuristics.nearest_neighbour(distances)
    shortInsertionSolutions, shortInsertionShortest = Heuristics.insertion(distances, "shortest")
    longInsertionSolutions, longInsertionShortest = Heuristics.insertion(distances, "longest")
    cheapInsertionSolutions, cheapInsertionShortest = Heuristics.insertion(distances, "cheapest")
    convexHullInsertionSolutions, convexHullInsertionShortest = Heuristics.insertion(distances, "ConvexHull")
    estimate = Heuristics.estimate(distances)
    print("Estimate for shortest")
    print(estimate)
    print("20% larger")
    print(round(estimate * 1.2))
    print("Brute Force")
    print(bruteShortest)
    print("Nearest Neighbour")
    print(nearestShortest)
    print("Shortest Insertion")
    print(shortInsertionShortest)
    print("Longest Insertion")
    print(longInsertionShortest)
    print("Cheapest Insertion")
    print(cheapInsertionShortest)
    print("Convex Insertion")
    print(convexHullInsertionShortest)
    while True:
        xValue = 1200
        yValue = 800
        runs = 0
        diff = 50
        pygame.init()
        screen = pygame.display.set_mode([xValue, yValue])
        running = True
        while True:
            try:
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    screen.fill((0, 0, 0))
                    # Brute Force
                    # xDiff and yDiff here are used to place the Heuristic in the correct location on the screen
                    speed = 0
                    for y in range(6):
                        if y == 0:
                            checkingSolutions = bruteSolutions
                            checkingShortest = bruteShortest
                            xDiff, yDiff = 50, 50
                        elif y == 1:
                            checkingSolutions = nearestSolutions
                            checkingShortest = nearestShortest
                            xDiff, yDiff = xValue // 3 + diff, 50
                        elif y == 2:
                            checkingSolutions = shortInsertionSolutions
                            checkingShortest = shortInsertionShortest
                            xDiff, yDiff = 2 * (xValue // 3) + diff, 50
                        elif y == 3:
                            checkingSolutions = longInsertionSolutions
                            checkingShortest = longInsertionShortest
                            xDiff, yDiff = 50, yValue // 2 + diff
                        elif y == 4:
                            checkingSolutions = cheapInsertionSolutions
                            checkingShortest = cheapInsertionShortest
                            xDiff, yDiff = xValue // 3 + diff, yValue // 2 + diff
                        else:
                            checkingSolutions = convexHullInsertionSolutions
                            checkingShortest = convexHullInsertionShortest
                            xDiff, yDiff = 2 * (xValue // 3) + diff, yValue // 2 + diff
                        # Draw all the nodes using x and y Diff so that nodes in the same Heuristic are altered by
                        # the same amount
                        for x in coordinates:
                            pygame.draw.circle(screen, (255, 0, 0), (x[0] + xDiff, x[1] + yDiff), 5)
                        # runs tells us which iteration in the Heuristics calculation to display
                        if runs < len(checkingSolutions):
                            previous = checkingSolutions[runs][0]
                            total = 0
                            for x in checkingSolutions[runs]:
                                if value and previous == x:
                                    # Important - can't remember why - something with the log function
                                    colour = (0, 255, 255)
                                elif value:
                                    # Logarithmic colour gradient for the "weight" of connections
                                    total = round(math.log(distances[previous][x - 1]) ** 2 * 3.5)
                                    colour = (255 - total, total, 255)
                                else:
                                    colour = (0, total, 255)
                                # Displays a line from the previous node in the current solution to the next one
                                pygame.draw.line(screen, colour,
                                                (adjust_to_centre(coordinates, previous - 1, xDiff, yDiff)),
                                                (adjust_to_centre(coordinates, x - 1, xDiff, yDiff)), 3)
                                previous = x
                                # Changes the colour but not very well
                                total += (255 // len(coordinates))
                            runs += 1
                        # When it has cycled thorough all the iterations of solutions it displays the best one that was found in a different colour
                        else:
                            previous = checkingShortest[1][0]
                            total = 0
                            for x in checkingShortest[1]:
                                if value and previous == x:
                                    # Important - can't remember why - something with the log function
                                    colour = (255, 0, 255)
                                elif value:
                                    total = round(math.log(distances[previous][x - 1]) ** 2 * 3.5)
                                    colour = (255, 255 - total, total)
                                else:
                                    colour = (total, (255 - total // 2), 0)
                                pygame.draw.line(screen, colour,
                                                 (adjust_to_centre(coordinates, previous - 1, xDiff, yDiff)),
                                                 (adjust_to_centre(coordinates, x - 1, xDiff, yDiff)), 3)
                                previous = x
                                total += (255 // len(coordinates))

                        if runs > len(checkingSolutions):
                            speed += 1

                    pygame.display.flip()
                    # I tried to get it to pause at the start so that it would be easier to see the start of the animation - I don't know why this isn't working
                    if len(coordinates) > 20:
                        sleep(0.2 / (2 ** speed))
                    else:
                        sleep(0.1)
            except KeyboardInterrupt:
                print("Closing...")
        # if yes is entered it will display the animation again
            if input("Again? ") != "yes":
                pygame.quit()
                break
            else:
                sleep(2)
