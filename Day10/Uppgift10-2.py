# --- Part Two ---

# It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, and the X register
# sets the horizontal position of the middle of that sprite. (In this system, there is no such thing as "vertical position": if the sprite's
#  horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)

# You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the row below that,
# and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.

# Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws a single pixel during each cycle. Representing each pixel of the
# screen as a #, here are the cycles during which the first and last pixel in each row are drawn:

# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120
# Cycle 121 -> ######################################## <- Cycle 160
# Cycle 161 -> ######################################## <- Cycle 200
# Cycle 201 -> ######################################## <- Cycle 240

# So, by carefully timing the CPU instructions and the CRT drawing operations, you should be able to determine whether the sprite is visible
# the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen
# produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

# The first few pixels from the larger example above are drawn as follows:

# # See input2Test.txt

# Allowing the program to run to completion causes the CRT to produce the following image:

# ##..##..##..##..##..##..##..##..##..##..
# ###...###...###...###...###...###...###.
# ####....####....####....####....####....
# #####.....#####.....#####.....#####.....
# ######......######......######......####
# #######.......#######.......#######.....

# Render the image given by your program. What eight capital letters appear on your CRT?

# Your puzzle answer was FECZELHE.

signalStrengthDictionary = {}


def ReadInputFile(url):
    X = 1
    cycleCount = 0

    for line in open(url):

        row = line.strip().split(" ")
        operation = row[0]

        match operation:
            case "noop":
                cycleCount += 1
                signalStrengthDictionary[cycleCount] = X
            case "addx":
                cycleCount += 2
                signalStrengthDictionary[cycleCount - 1] = X
                signalStrengthDictionary[cycleCount] = X
                X += int(row[-1])


def Draw():

    for row in range(6):
        for column in range(40):
            cycle = column + 1 + 40 * row
            spritePos = signalStrengthDictionary[cycle]
            if spritePos - 1 <= column <= spritePos + 1:
                print("#", end="")
            else:
                print(".", end="")

        print("")


ReadInputFile("Day10/input10.txt")

Draw()
