# --- Part Two ---

# As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though;
# perhaps you can find a better starting point.

# To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E.
#
# However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from
# any square at elevation a to the square marked E.

# Again consider the example from above:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you
# start at the bottom-left square, you can reach the goal most quickly:

# ...v<<<<
# ...vv<<^
# ...v>E^^
# .>v>>>^^
# >^>>>>>^

# This path reaches the goal in only 29 steps, the fewest possible.

# What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

from collections import defaultdict
import heapq

input = open("Day12/input12.txt").read()
allRows = input.split("\n")
noOfCols = len(allRows[0])
noOfRows = len(allRows) - 1

myLetter = "a"
myPosition = (0, 0)


def FindPositionOfCharacter(characterToSearchFor):
    rowPos = -1
    colPos = -1
    position = (rowPos, colPos)
    for rowIndex in range(noOfRows):
        rowPos += 1
        row = allRows[rowIndex]
        colPos = str(row).find(characterToSearchFor)
        if colPos != -1:
            position = (rowPos, colPos)

    return position


def FindAllPositionsOfCharacter(characterToSearchFor):
    positions = []
    for rowIndex in range(noOfRows):
        for colIndex in range(noOfCols):
            if allRows[rowIndex][colIndex] == characterToSearchFor:
                positions.append((rowIndex, colIndex))

    return positions


positionDictionary = {}


def ConstructPositionDictionary():
    i = 0
    for rowIndex in range(noOfRows):
        for colIndex in range(noOfCols):
            positionDictionary[(rowIndex, colIndex)] = i
            i += 1


startingPosition = FindPositionOfCharacter("S")
print("The starting position is " + str(startingPosition))
destination = FindPositionOfCharacter("E")
print("The destination is " + str(destination))


def MapUpTheGraph():
    graph = []
    i = 0
    for rowIndex in range(noOfRows):
        for colIndex in range(noOfCols):
            graphIndex = positionDictionary[(rowIndex, colIndex)]
            graph.append([])

            possibleDestinations = [
                (rowIndex, colIndex - 1),
                (rowIndex - 1, colIndex),
                (rowIndex, colIndex + 1),
                (rowIndex + 1, colIndex),
            ]

            for destRow, destCol in possibleDestinations:
                if 0 <= destRow < noOfRows and 0 <= destCol < noOfCols:
                    possibleDestination = allRows[destRow][destCol]
                    if possibleDestination == "S":
                        possibleDestination = "a"
                    if possibleDestination == "E":
                        possibleDestination = "z"

                    myPosition = allRows[rowIndex][colIndex]
                    if myPosition == "S":
                        myPosition = "a"
                    if myPosition == "E":
                        myPosition = "z"

                    if ord(possibleDestination) <= ord(myPosition) + 1:
                        possibleDestGraphIndex = positionDictionary[(destRow, destCol)]
                        graph[graphIndex].append(possibleDestGraphIndex)
                        i += 1

    return graph


def dijkstra(graph, start):
    result_map = [float("inf")] * len(graph)
    result_map[start] = 0
    visited = [False] * len(graph)
    queue = [(0, start)]

    while queue:
        weight, v = heapq.heappop(queue)
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                newWeight = 1 + weight
                if newWeight < result_map[u]:
                    result_map[u] = newWeight
                    heapq.heappush(queue, [1 + weight, u])

    return result_map


startingPosition = FindPositionOfCharacter("a")


ConstructPositionDictionary()
print("positionDictionary: " + str(positionDictionary))

destinationGraph = MapUpTheGraph()
print("Graph is mapped.")


possibleStartingPositions = FindAllPositionsOfCharacter("a")
possibleResults = []
for startPos in possibleStartingPositions:
    start = positionDictionary[startPos]

    result = dijkstra(destinationGraph, start)
    dest = positionDictionary[destination]
    possibleResults.append(result[dest])

print(possibleResults)
possibleResults.sort()
print("Number of steps in the way: " + str(possibleResults[0]))
