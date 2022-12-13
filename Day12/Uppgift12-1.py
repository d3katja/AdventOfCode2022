# --- Day 12: Hill Climbing Algorithm ---

# You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

# You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid;
# the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current
# position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down,
#  left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation
# of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation
# of the destination square can be much lower than the elevation of your current square.)

# For example:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head
# toward the e at the bottom. From there, you can spiral around to the goal:

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^

# In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location
# that should get the best signal is still E, and . marks unvisited squares.

# This path reaches the goal in 31 steps, the fewest possible.

# What is the fewest steps required to move from your current position to the location that should get the best signal?

# Strategy: 1) Find out which letter you stand on. 2) Look at the letters right, below, left and above you. 3) If the letter is one higher than
# your letter, go there and increment steps with one. Else go to the letter that is the same as you. 3) If you cannot find a letter you need to back
# one step to where you were before and try another route. For this your last position needs to be saved so you can retrace. If you retrace, decrement
# your steps.

# Your puzzle answer was 440.

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


ConstructPositionDictionary()
print("positionDictionary: " + str(positionDictionary))

destinationGraph = MapUpTheGraph()
print("Graph is mapped.")
startPos = positionDictionary[startingPosition]
result = dijkstra(destinationGraph, startPos)
print(result)
dest = positionDictionary[destination]
print("Number of steps in the way: " + str(result[dest]))
