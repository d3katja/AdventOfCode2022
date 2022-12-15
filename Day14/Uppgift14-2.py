input = open("Day14/input14.txt").read().strip()
allRows = input.split("\n")
noOfRows = len(allRows) - 1
positions = set()
sandHole = (500, 0)


def AddLine(p1, p2):
    if p1[0] == p2[0]:
        start = min(p1[1], p2[1])
        slut = max(p1[1], p2[1]) + 1
        for y in range(start, slut):
            newPoint = (p1[0], y)
            positions.add(newPoint)

    else:
        start = min(p1[0], p2[0])
        slut = max(p1[0], p2[0]) + 1
        for x in range(start, slut):
            newPoint = (x, p1[1])
            positions.add(newPoint)


for row in allRows:
    pos = row.split(" -> ")
    #    print("pos: " + str(pos))
    rowPositions = []
    for r in pos:
        ps = r.split(",")
        p = (int(ps[0]), int(ps[1]))
        #        print("p: " + str(p))
        rowPositions.append(p)
    apa = zip(rowPositions, rowPositions[1:])

    for (p1, p2) in apa:
        AddLine(p1, p2)
print("positions: " + str(positions))


def SandFallsDownRight(sandPosition):
    newPosition = (sandPosition[0] + 1, sandPosition[1] + 1)
    #    print("SandFallsDownRight / newPosition: " + str(newPosition))

    if newPosition[1] == maxYPosition:
        # The sand is falling into eternity, we are done.
        print("The sand is falling into eternity, we are done.")
        positions.add(sandPosition)
        return True

    if newPosition not in positions:
        return SandFallsOneRowDown(newPosition)
    else:
        positions.add(sandPosition)
        #        print("Sand stopped at: " + str(sandPosition))
        return sandPosition != sandHole


def SandFallsDownLeft(sandPosition):
    newPosition = (sandPosition[0] - 1, sandPosition[1] + 1)
    #    print("SandFallsDownLeft / newPosition: " + str(newPosition))

    if newPosition[1] == maxYPosition:
        # The sand is falling into eternity, we are done.
        positions.add(sandPosition)
        return True

    if newPosition not in positions:
        return SandFallsOneRowDown(newPosition)
    else:
        return SandFallsDownRight(sandPosition)


def SandFallsOneRowDown(sandPosition):
    newPosition = (sandPosition[0], sandPosition[1] + 1)
    #    print("SandFallsOneRowDown / newPosition: " + str(newPosition))

    if newPosition[1] == maxYPosition:
        # The sand is falling into eternity, we are done.
        positions.add(sandPosition)
        return True

    if newPosition not in positions:
        return SandFallsOneRowDown(newPosition)
    else:
        return SandFallsDownLeft(sandPosition)


maxYPosition = max([y for (_, y) in positions]) + 2

sandUnits = 1
while SandFallsOneRowDown(sandHole):
    sandUnits += 1

print("sandUnits: " + str(sandUnits))
