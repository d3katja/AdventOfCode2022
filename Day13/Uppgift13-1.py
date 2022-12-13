# --- Day 13: Distress Signal ---

# You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting: a distress signal.

# Your handheld device must still not be working properly; the packets from the distress signal got decoded out of order. You'll need
# to re-order the list of received packets (your puzzle input) to decode the message.

# Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify how many pairs of packets are in the right order.

# For example:
# # see test file.

# Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more comma-separated values
# (either integers or other lists). Each packet is always a list and appears on its own line.

# When comparing two values, the first value is called left and the second value is called right. Then:

#     If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs
# are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the
# inputs are the same integer; continue checking the next part of the input.
#     If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of
# items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If
# the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#     If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the
# comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by
# instead comparing [0,0,0] and [2].

# Using these rules, you can determine which of the pairs in the example are in the right order:

# What are the indices of the pairs that are already in the right order? (The first pair has index 1, the second pair has index 2, and
# so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.

# Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?

# Your puzzle answer was 5393.

import json

input = open("Day13/input13.txt").read()
allRows = input.split("\n")
noOfRows = len(allRows) - 1
# print(allRows[0])


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


result = 0
for rowIndex in range(0, noOfRows, 3):
    row1 = json.loads(allRows[rowIndex])
    row2 = json.loads(allRows[rowIndex + 1])
    print(row1)
    print(row2)
    comparisonResult = Compare(row1, row2)
    print("comparisonResult: " + str(comparisonResult))
    if comparisonResult == -1:
        result += ((rowIndex + 1) // 3) + 1

print("The result is " + str(result))
