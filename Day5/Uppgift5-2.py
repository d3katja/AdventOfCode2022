# --- Part Two ---

# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3

# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3

# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3

# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
# Your puzzle answer was JNRSCDWPP.

crateStacks = []
crateMoves = []
numberOfIndeces = 0


def Uppgift():

    for line in open("Day5/input5.txt"):
        row = line
        rightParenthesis = False

        crateStack = []

        crateIndeces = []  # [1, 5, 9, 13, 17, 21, 25, 29, 33]
        if row[0] == " " or row[0] == "[":
            length = len(row)
            numberOfIndeces = int(length / 4)

            for i in range(numberOfIndeces):
                if not crateIndeces or len(crateIndeces) < numberOfIndeces:
                    crateIndeces.append(i * 4 + 1)
                if not crateStacks or len(crateStacks) < numberOfIndeces:
                    crateStacks.append([])
                    print("crateIndeces: " + str(crateIndeces))

            j = 0
            for i in crateIndeces:
                crate = row[i]
                if crate.isalpha():
                    crateStacks[j].insert(0, crate)

                j += 1

        elif row[0] == "m":
            # this is a moving line
            HandleMoveLine(row)

    print("Uppgift crateStacks: " + str(crateStacks))
    print("Uppgift crateMoves: " + str(crateMoves))
    MoveCrates()


def HandleMoveLine(row):
    moves = (
        row.replace("move", "").replace("from", "").replace("to", "").strip().split(" ")
    )
    moveList = [moves[0], moves[2], moves[4]]
    crateMoves.append(moveList)


def MoveCrates():
    for move in crateMoves:
        noOfCratesToMove = int(move[0])
        stackToMoveFrom = int(move[1]) - 1
        stackToMoveTo = int(move[2]) - 1
        print(move)
        print("MoveCrates crateStacks before move: " + str(crateStacks))
        temp = []
        for i in range(noOfCratesToMove):
            temp.append(crateStacks[stackToMoveFrom].pop())
        temp.reverse()
        crateStacks[stackToMoveTo].extend(temp)
        print("MoveCrates crateStacks after move: " + str(crateStacks))


Uppgift()
print("Result: " + "".join([s[-1] for s in crateStacks]))
