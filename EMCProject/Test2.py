def recur(lis, nodes, notVisited, total):
    if len(notVisited) > 1:
        for i in notVisited:
            nodes[1].append(i)
            notVisited.remove(i)
            # check here
            total = recur(lis, nodes, notVisited, total)
        notVisited.append(nodes[1][-1])
        nodes[1].pop()
        notVisited.sort()
    else:
        nodes[1].append(notVisited[0])
        nodes[1].append(1)
        total += 1
        # checkl here - final output
        notVisited.append(nodes[1][-3])
        for x in range(3):
            nodes[1].pop()
        notVisited.sort()
    return total



nodes = [0, [1]]
num = 3
lisOfNodes = []
for x in range(1, num+1):
    lisOfNodes.append(x)
notVistited = lisOfNodes[1:]


print(recur(lisOfNodes, nodes, notVistited, 0))
