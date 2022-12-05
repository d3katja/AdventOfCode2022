# --- Day 5: Supply Stacks ---

# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates,
# but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane
# operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top
# of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where,
# and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]
# [N] [C]
# [Z] [M] [P]
# 1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2
# contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack.
# In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]
# [N] [C]
# [Z] [M] [P]
# 1   2   3

# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up
# below the second and third crates:

#        [Z]
#        [N]
#    [C] [D]
#    [M] [P]
# 1   2   3

# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#          [Z]
#          [N]
#  [M]     [D]
#  [C]     [P]
#   1   2   3

# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
# 1   2   3

# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2,
# and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

# To begin, get your puzzle input.
# Your puzzle answer was TWSGQHNHL.

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
        for i in range(noOfCratesToMove):
            crate = crateStacks[stackToMoveFrom].pop()
            crateStacks[stackToMoveTo].append(crate)
        print("MoveCrates crateStacks after move: " + str(crateStacks))


Uppgift()
print("Result: " + "".join([s[-1] for s in crateStacks]))
