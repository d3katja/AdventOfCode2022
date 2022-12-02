# --- Part Two ---

# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column
# says how the round needs to end: X means you need to lose, Y means you need to end the round in
# a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to
# choose so the round ends as indicated. The example above now goes like this:

#     In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y),
# so you also choose Rock. This gives you a score of 1 + 3 = 4.
#     In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#     In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

# Following the Elf's instructions for the second column, what would your total score be if everything
# goes exactly according to your strategy guide?
# Your puzzle answer was 8295.

rockPoint = 1
paperPoint = 2
scissorsPoint = 3
losingPoint = 0
drawPoint = 3
winPoint = 6
totalPoints = 0

for line in open("Day2/input2.txt"):
    gameRow = line.strip()

    if gameRow:
        gamePoint = 0
        opponentMove = gameRow[0]
        wantedResult = gameRow[2]

        print(opponentMove)
        myMove = ""
        match wantedResult:
            case "X":
                print("The opponent won.")
                gamePoint += losingPoint
                print("gamePoint: " + str(gamePoint))
                match opponentMove:
                    case "A":
                        myMove = "C"
                    case "B":
                        myMove = "A"
                    case "C":
                        myMove = "B"

            # It's a draw.
            case "Y":
                print("It's a draw.")
                gamePoint += drawPoint
                print("gamePoint: " + str(gamePoint))
                myMove = opponentMove

            # I won.
            case "Z":
                print("I won.")
                gamePoint += winPoint
                print("gamePoint: " + str(gamePoint))
                match opponentMove:
                    case "A":
                        myMove = "B"
                    case "B":
                        myMove = "C"
                    case "C":
                        myMove = "A"

        print("myMove: " + myMove)
        match myMove:
            case "A":
                gamePoint += rockPoint
            case "B":
                gamePoint += paperPoint
            case "C":
                gamePoint += scissorsPoint

    print("gamePoint: " + str(gamePoint))
    totalPoints += gamePoint

print(totalPoints)
