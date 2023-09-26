import random

class nodes:
    def __init__(self, id, randomlyGenerate, numberOfConnections = 0, rangeOfConnections = 0):
        self.number = id
        self.connected = False
        self.final = False
        self.connectedTo = None
        self.possibleConnections = []
        if randomlyGenerate:
            for x in range(random.randint(1, numberOfConnections)):
                new = random.randint(0, rangeOfConnections - 1)
                if new not in self.possibleConnections:
                    self.possibleConnections.append(new)

    def __str__(self):
        return f"{self.number}\nconnected = {self.connected}\nconnectedTo = {self.connectedTo}\n{self.possibleConnections}"


numberOfNodes = 5
firstNodes = []
secondNodes = []
for x in range(numberOfNodes):
    firstNodes.append(nodes(x, True, 4, numberOfNodes))
    secondNodes.append(nodes(x, False))
for x in range(len(firstNodes)):
    for item in firstNodes[x].possibleConnections:
        secondNodes[item].possibleConnections.append(firstNodes[x].number)


# Make it so that it checks if the node.final == True
# If it is otherwise connected then change those connections
action = True
while action:
    action = False
    for item in firstNodes:
        if not item.connected and len(item.possibleConnections) == 1:
            action = True
            item.connected = True
            if not secondNodes[item.possibleConnections[0]].connected:
                item.connectedTo = item.possibleConnections[0]
                secondNodes[item.connectedTo].connected = True
                secondNodes[item.connectedTo].connectedTo = item.number
                for connection in firstNodes:
                    if connection.number != item.number:
                        if item.possibleConnections[0] in connection.possibleConnections:
                            connection.possibleConnections.remove(item.possibleConnections[0])

