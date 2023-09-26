def calculate_path_length(dists, nodes):
    total = 0
    previous = nodes[0]
    for i in nodes:
        total += dists[previous][i - 1]
        previous = i
    return total


# A function called by the update_path function to add the distance between nodes to the running total when a node is added to the current selection being tested
def update_path_length(dists, nodes):
    if len(nodes[1]) > 1:
        last = nodes[1][-2]
        current = nodes[1][-1] - 1
        return dists[last][current]
    else:
        return 0


# A recursive function called by the brute force function
def update_path(dists, short, lis, nodes, notVisited, solutions):
    if len(notVisited) > 1:
        for i in notVisited:
            nodes[1].append(i)
            notVisited.remove(i)
            nodes[0] += update_path_length(dists, nodes)
            if short[0] > nodes[0]:
                update_path(dists, short, lis, nodes, notVisited, solutions)
            else:
                notVisited.append(nodes[1][-1])
                nodes[0] -= update_path_length(dists, nodes)
                nodes[1].pop()
                notVisited.sort()

        notVisited.append(nodes[1][-1])
        nodes[0] -= update_path_length(dists, nodes)
        nodes[1].pop()
        notVisited.sort()

    else:
        nodes[1].append(notVisited[0])
        nodes[0] += update_path_length(dists, nodes)
        nodes[1].append(1)
        nodes[0] += update_path_length(dists, nodes)
        nodes[0] = round(nodes[0], 6)

        if short[0] > round(nodes[0], 6):
            short[0] = round(nodes[0], 6)
            short[1] = nodes[1][:]
            solutions.append(short[1])
        notVisited.append(nodes[1][-3])
        for x in range(3):
            nodes[0] -= update_path_length(dists, nodes)
            nodes[1].pop()
        notVisited.sort()


# The function called to run the brute force algorithm
# Inputs the dictionary of distances between nodes
# Outputs the shortest path and the nodes in that path found by the brute force algorithm
# It works by calling a recussive function which will call itself if there are still unvistited nodes allowing every combination to be checked


def brute_force(distances):
    shortestPath = [2147483647, []]
    currentPath = [0, [1]]
    num = len(distances[1])
    lisOfNodes = []
    solutions = []
    for x in range(1, num + 1):
        lisOfNodes.append(x)
    notVisited = lisOfNodes[1:]
    update_path(distances, shortestPath, lisOfNodes, currentPath, notVisited, solutions)
    return solutions, shortestPath


def nearest_neighbour(distances):
    shortest = [2147483647, []]
    nodes = []
    solutions = []
    num = len(distances)
    for x in range(1, num + 1):
        nodes.append(x)
    for j in nodes:
        currentPath = [0, [j]]
        lisOfNodes = nodes.copy()
        lisOfNodes.remove(j)
        for x in range(num - 1):
            short = [2147483647, 0]
            for i in lisOfNodes:
                length = distances[(currentPath[1][-1])][i - 1]
                if length < short[0]:
                    short = [length, i]
            lisOfNodes.remove(short[1])
            currentPath[1].append(short[1])
        currentPath[1].append(j)
        currentPath[0] = round(calculate_path_length(distances, currentPath[1]), 4)

        solutions.append(currentPath[1])
        if currentPath[0] < shortest[0]:
            shortest = currentPath.copy()
    return solutions, shortest


def insertion(distances, insertionType):
    shortestPath = [2147483647, []]
    pathsTaken = []
    for number in distances:
        path = [number, number]
        for x in range(len(distances) - 1):
            if insertionType == "cheapest" or insertionType == "ConvexHull":
                best = [0, 0, 2147483647]
                for index in range(1, len(path)):
                    for item in distances:
                        if item not in path:
                            if insertionType == "cheapest":
                                current = distances[path[index - 1]][item - 1] + distances[item][path[index] - 1] - distances[path[index - 1]][path[index] - 1]
                            else:
                                if distances[path[index - 1]][path[index] - 1] == 0:
                                    ratio = 1
                                else:
                                    ratio = distances[path[index - 1]][path[index] - 1]
                                current = (distances[path[index - 1]][item - 1] + distances[item][path[index] - 1]) // ratio
                            if current < best[2]:
                                best = [item, index, current]
            else:
                if insertionType == "shortest":
                    best = [0, 0, 2147483647]
                elif insertionType == "longest":
                    best = [0, 0, -1]
                else:
                    best = []
                    print("Things have gone very badly wrong")

                for index in range(1, len(path)):
                    for item in distances:
                        if item not in path:
                            current = distances[path[index - 1]][item - 1]
                            if (insertionType == "shortest" and current < best[2]) or (insertionType == "longest" and current > best[2]):
                                best = [item, index, current]

            newPath = []
            for item in path[:(best[1])]:
                newPath.append(item)
            newPath.append(best[0])
            for item in path[best[1]:]:
                newPath.append(item)
            path = newPath
            pathsTaken.append(path)
        length = round(calculate_path_length(distances, pathsTaken[-1]), 4)
        if length < shortestPath[0]:
            shortestPath = [length, pathsTaken[-1]]
    return pathsTaken, shortestPath


def estimate(distances):
    total = 0
    for item in distances:
        smallest = 2147483647
        nextSmallest = 2147483647
        for value in distances[item]:
            if value < smallest:
                smallest, nextSmallest = value, smallest
            elif value < nextSmallest:
                nextSmallest = value
        total += (smallest + nextSmallest) // 2
    return total

