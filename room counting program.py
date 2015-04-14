__author__ = 'macuser'
illustration = []
row_counter = 0
room_counter = 0
# we will make rooms fill with "s" and non rooms fill with "e"
loop_breaker = 0
iterate_row = 0
iterate_collum = 0
fill_with = ","

done = 0

#make lits of lists
with open("roommap.txt", "r") as map:
    for line in map:
        illustration.append([])
        row_counter = row_counter + 1
        for character in line:
            if character != '\n':
                illustration[-1].append(character)

row_start_point = 0

collum_start_point = 0

row = row_start_point
collum = collum_start_point


def place_start_point(row, collum):
    while illustration[row][collum] != '.':
        if row < row_counter - 1:
            row = row + 1

        else:
            collum = collum + 1
            row = 0

            if collum == len(line):
                loop_breaker = 1
                break

    return row, collum


def check(row, collum):
    if row < row_counter and collum < len(line) and row > -1 and collum > -1:
        if illustration[row][collum] == 'X' or illustration[row][collum] == '>' or illustration[row][collum] == '#' or \
                        illustration[row][collum] == ",":
            return
        else:
            illustration[row][collum] = fill_with

            check(row + 1, collum)
            check(row, collum + 1)
            check(row, collum - 1)
            check(row - 1, collum)
    else:

        return


check(row, collum)

fill_with = ">"

row = 0
collum = 0

row, collum = place_start_point(row, collum)

while loop_breaker == 0:
    # print row
    # print collum
    # print illustration[row][collum]
    # print row_counter
    # print len(line)
    row, collum = place_start_point(row, collum)
    check(row, collum)
    if collum == len(line):
        break
    row = 0
    collum = 0
    room_counter = room_counter + 1

for row in illustration:
    print "".join(row)
if room_counter == 1:
    print "There is one room"
else:
    print "There are %s rooms" % (room_counter)

