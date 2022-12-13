# --- Part Two ---

# Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.

# The distress signal protocol also requires that you include two additional divider packets:

# [[2]]
# [[6]]

# Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.

# For the example above, the result of putting the packets in the correct order is:

# []
# [[]]
# [[[]]]
# [1,1,3,1,1]
# [1,1,5,1,1]
# [[1],[2,3,4]]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [[1],4]
# [[2]]
# [3]
# [[4,4],4,4]
# [[4,4],4,4,4]
# [[6]]
# [7,7,7]
# [7,7,7,7]
# [[8,7,6]]
# [9]

# Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) In this example, the divider packets are 10th and 14th, and so the decoder key is 140.

# Organize all of the packets into the correct order. What is the decoder key for the distress signal?

# Your puzzle answer was 26712.

from functools import cmp_to_key
import json

input = open("Day13/input13.txt").read()
allRows = input.split("\n")
allRows = [json.loads(value) for value in allRows if value]
allRows.append([[2]])
allRows.append([[6]])
noOfRows = len(allRows) - 1


def Compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left == right:
            return 0
        else:
            return 1

    if isinstance(left, int):
        return Compare([left], right)

    if isinstance(right, int):
        return Compare(left, [right])

    for (l, r) in zip(left, right):
        result = Compare(l, r)
        if result != 0:
            return result
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


sortedRows = sorted(allRows, key=cmp_to_key(Compare))
index2 = sortedRows.index([[2]]) + 1
index6 = sortedRows.index([[6]]) + 1
result = index2 * index6

# for rowIndex in range(noOfRows):
#     row1 = json.loads(allRows[rowIndex])

#     row2 = json.loads(allRows[rowIndex + 1])
#     print(row1)
#     print(row2)
#     comparisonResult = Compare(row1, row2)
#     print("comparisonResult: " + str(comparisonResult))
#     if comparisonResult == -1:
#         result += ((rowIndex + 1) // 3) + 1

print("The result is " + str(result))
