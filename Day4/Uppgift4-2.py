# --- Part Two ---

# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the
# number of pairs that overlap at all.

# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs
# (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

#     5-7,7-9 overlaps in a single section, 7.
#     2-8,3-7 overlaps all of the sections 3 through 7.
#     6-6,4-6 overlaps in a single section, 6.
#     2-6,4-8 overlaps in sections 4, 5, and 6.

# So, in this example, the number of overlapping assignment pairs is 4.

# In how many assignment pairs do the ranges overlap?
# Your puzzle answer was 770.

numberOfPairsThatOverlapSomewhat = 0
rowNumber = 0

for line in open("Day4/input4.txt"):
    rowNumber += 1
    contents = line.strip().split(",")
    elf1Assignment = contents[0].split("-")
    elf2Assignment = contents[1].split("-")

    print("numberOfPairsThatOverlapSomewhat: " + str(numberOfPairsThatOverlapSomewhat))
    print(elf1Assignment)
    print(elf2Assignment)

    if (
        int(elf1Assignment[0]) <= int(elf2Assignment[0])
        and int(elf1Assignment[1]) >= int(elf2Assignment[0])
        or int(elf2Assignment[0]) <= int(elf1Assignment[0])
        and int(elf2Assignment[1]) >= int(elf1Assignment[0])
    ):
        numberOfPairsThatOverlapSomewhat += 1
        print("Found overlapping pair on row " + str(rowNumber))

print("numberOfPairsThatOverlapSomewhat: " + str(numberOfPairsThatOverlapSomewhat))
print("rowNumber: " + str(rowNumber))
