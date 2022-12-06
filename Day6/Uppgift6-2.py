# --- Part Two ---

# Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

# Here are the first positions of start-of-message markers for all of the above examples:

#     mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
#     bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
#     nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
#     nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
#     zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

# How many characters need to be processed before the first start-of-message marker is detected?

# Your puzzle answer was 3965.

# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # first marker after character 19 == index + 4
# input = "bvwbjplbgvbhsrlpgdmjqwftvncz"  # first marker after character 23
# input = "nppdvjthqldpwncqszvftbrmjlhg"  # first marker after character 23
# input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"  # first marker after character 29
# input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # first marker after character 26

input = open("Day6/input6.txt").read()

lastIndex = len(input)

for i in range(lastIndex - 14):
    chop = input[i : i + 14]
    chopWithoutDuplicates = set(chop)
    print("chop: " + chop)
    print("chopWithoutDuplicates: " + "".join(chopWithoutDuplicates))

    if len("".join(chopWithoutDuplicates)) == 14:
        # We have found the marker.
        firstStartOfPacketMarker = i + 14
        print(firstStartOfPacketMarker)
        break
