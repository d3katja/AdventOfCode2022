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

input = open("Day8/inputTest8.txt").read()
allRows = input.split("\n")
allRowsTest = allRows.pop()
rowLength = len(allRows[0])
noOfRows = len(allRows)
lastRowIndex = int(len(input) / rowLength) - 1
print("Number of rows in file: " + str(noOfRows))
print("Number of columns per row: " + str(rowLength))


def Uppgift():
    totalNumberOfVisibleTrees = 2 * rowLength + 2 * (noOfRows - 2)
    print("totalNumberOfVisibleTrees from the start: " + str(totalNumberOfVisibleTrees))
    foundTreePositions = []

    for rowIndex in range(1, lastRowIndex - 1):
        currentRow = allRows[rowIndex]
        print("currentRow: " + currentRow)
        numberOfVisibleTrees = 0
        highestTreeFromLeft = int(allRows[rowIndex][0])
        highestTreeFromLeftPosition = (rowIndex, int(0))
        highestTreeFromRight = int(allRows[0][rowLength - 1])
        highestTreeFromRightPosition = (rowIndex, int(rowLength - 1))

        for colIndex in range(1, rowLength - 2):
            currentPos = int(allRows[rowIndex][colIndex])
            previousPos = int(allRows[rowIndex][colIndex - 1])
            if currentPos > previousPos and currentPos > highestTreeFromLeft:
                highestTreeFromLeft = currentPos
                highestTreeFromLeftPosition = (rowIndex, colIndex)
                print(
                    "highestTreeFromLeftPosition: " + str(highestTreeFromLeftPosition)
                )
                numberOfVisibleTrees += 1
                foundTreePositions.append(highestTreeFromLeftPosition)

        for colIndex in range(rowLength - 2, 1, -1):
            currentPos = int(allRows[rowIndex][colIndex])
            previousPos = int(allRows[rowIndex][colIndex + 1])
            if currentPos > previousPos and currentPos > highestTreeFromRight:
                highestTreeFromRight = currentPos
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

    # TODO: Check that the found positions are not already found.
    for colIndex in range(1, rowLength - 1):
        numberOfVisibleTrees = 0
        highestTreeFromTop = int(allRows[0][colIndex])
        highestTreeFromTopPosition = (int(0), colIndex)
        highestTreeFromBottom = int(allRows[lastRowIndex - 1][colIndex])
        highestTreeFromBottomPosition = (int(lastRowIndex - 1), colIndex)

        for rowIndex in range(1, lastRowIndex - 1):
            currentPos = int(allRows[rowIndex][colIndex])
            previousPos = int(allRows[rowIndex - 1][colIndex])
            if currentPos > previousPos and currentPos > highestTreeFromRight:
                highestTreeFromTop = currentPos
                highestTreeFromTopPosition = (rowIndex, colIndex)
                print("highestTreeFromTopPosition: " + str(highestTreeFromTopPosition))
                if not highestTreeFromTopPosition in foundTreePositions:
                    numberOfVisibleTrees += 1
                    foundTreePositions.append(highestTreeFromTopPosition)

        for rowIndex in range(lastRowIndex - 1, 1, -1):
            currentPos = int(allRows[rowIndex][colIndex])
            previousPos = int(allRows[rowIndex + 1][colIndex])
            if currentPos > previousPos and currentPos > highestTreeFromRight:
                highestTreeFromBottom = currentPos
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
