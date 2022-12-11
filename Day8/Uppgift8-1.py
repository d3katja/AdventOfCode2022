# --- Day 8: Treetop Tree House ---

# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted
# these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are
# visible from outside the grid when looking directly along a row or column.

# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

# 30373
# 25512     [1][]
# 65332
# 33549
# 35390

# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column;
# that is, only look up, down, left, or right from any given tree.

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example,
# that only leaves the interior nine trees to consider:

#     The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
#     The top-middle 5 is visible from the top and right.
#     The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
#     The left-middle 5 is visible, but only from the right.
#     The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
#     The right-middle 3 is visible from the right.
#     In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

# Consider your map; how many trees are visible from outside the grid?

# Your puzzle answer was 1703.

input = open("Day8/input8.txt").read()
allRows = input.split("\n")
rowLength = len(allRows[0])
noOfRows = len(allRows) - 1
lastRowIndex = int(len(input) / rowLength) - 1
print("Number of rows in file: " + str(noOfRows))
print("Number of columns per row: " + str(rowLength))


def Uppgift():
    totalNumberOfVisibleTrees = 0
    print("totalNumberOfVisibleTrees from the start: " + str(totalNumberOfVisibleTrees))
    foundTreePositions = []

    for rowIndex in range(0, lastRowIndex):
        currentRow = allRows[rowIndex]
        print("currentRow: " + currentRow)
        numberOfVisibleTrees = 0
        highestTreeFromLeft = -1

        for colIndex in range(rowLength):
            currentHeight = int(allRows[rowIndex][colIndex])
            previousHeight = -1
            if currentHeight > previousHeight and currentHeight > highestTreeFromLeft:
                highestTreeFromLeft = currentHeight
                highestTreeFromLeftPosition = (rowIndex, colIndex)
                print(
                    "highestTreeFromLeftPosition: " + str(highestTreeFromLeftPosition)
                )
                if not highestTreeFromLeftPosition in foundTreePositions:
                    numberOfVisibleTrees += 1
                    foundTreePositions.append(highestTreeFromLeftPosition)

        highestTreeFromRight = -1
        for colIndex in reversed(range(rowLength)):
            currentHeight = int(allRows[rowIndex][colIndex])
            previousHeight = -1
            if currentHeight > previousHeight and currentHeight > highestTreeFromRight:
                highestTreeFromRight = currentHeight
                highestTreeFromRightPosition = (rowIndex, colIndex)
                print(
                    "highestTreeFromRightPosition: " + str(highestTreeFromRightPosition)
                )
                if not highestTreeFromRightPosition in foundTreePositions:
                    numberOfVisibleTrees += 1
                    foundTreePositions.append(highestTreeFromRightPosition)

        print("numberOfVisibleTrees: " + str(numberOfVisibleTrees))
        totalNumberOfVisibleTrees += numberOfVisibleTrees
        print("totalNumberOfVisibleTrees: " + str(totalNumberOfVisibleTrees))

    for colIndex in range(rowLength):
        numberOfVisibleTrees = 0

        highestTreeFromTop = -1
        for rowIndex in range(0, lastRowIndex):
            currentHeight = int(allRows[rowIndex][colIndex])
            if currentHeight > highestTreeFromTop:
                highestTreeFromTop = currentHeight
                highestTreeFromTopPosition = (rowIndex, colIndex)
                print("highestTreeFromTopPosition: " + str(highestTreeFromTopPosition))
                if not highestTreeFromTopPosition in foundTreePositions:
                    numberOfVisibleTrees += 1
                    foundTreePositions.append(highestTreeFromTopPosition)

        highestTreeFromBottom = -1
        for rowIndex in reversed(range(lastRowIndex)):
            currentHeight = int(allRows[rowIndex][colIndex])
            if currentHeight > highestTreeFromBottom:
                highestTreeFromBottom = currentHeight
                highestTreeFromBottomPosition = (rowIndex, colIndex)
                print(
                    "highestTreeFromBottomPosition: "
                    + str(highestTreeFromBottomPosition)
                )
                if not highestTreeFromBottomPosition in foundTreePositions:
                    numberOfVisibleTrees += 1
                    foundTreePositions.append(highestTreeFromBottomPosition)

        print("numberOfVisibleTrees: " + str(numberOfVisibleTrees))
        totalNumberOfVisibleTrees += numberOfVisibleTrees
        print("totalNumberOfVisibleTrees: " + str(totalNumberOfVisibleTrees))

    print("totalNumberOfVisibleTrees at the end: " + str(totalNumberOfVisibleTrees))


Uppgift()
