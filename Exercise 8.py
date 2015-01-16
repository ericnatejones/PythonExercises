row_start_point = 21
collum_start_point = 21
while row_start_point < -1 or row_start_point > 12:
    row_start_point = int(raw_input("What row to start in(0 to 12)"))

while collum_start_point < -1 or collum_start_point > 19:
    collum_start_point = int(raw_input("What collum to start in(0 to 19)"))

illustration = [
['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','X','X','X','X','X','X','X','X','X','X','.','.','.'],
['.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','X','.','.','.'],
['.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','X','.','.','.'],
['.','.','X','X','X','X','X','X','.','.','.','.','.','.','.','.','X','.','.','.'],
['.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','.','.'],
['.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','X','.','.','.'],
['.','.','X','.','.','.','.','.','.','.','.','X','X','X','X','X','X','.','.','.'],
['.','.','X','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.'],
['.','.','X','X','X','X','.','.','X','X','X','X','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','X','X','X','X','.','.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
]

row = row_start_point
collum = collum_start_point

# illustration [row][collum] = "W"

# this loop will help the start point not be an X

while illustration[row][collum] == "X":
    row = row + 1
    print "loop"


def check(row,collum):
    if row < 13 and collum < 20 and row > -1 and collum > -1:
        if illustration[row][collum] == 'X' or illustration[row][collum] =='s':
            return
        else:
            illustration[row][collum] = "s"

            check(row+1,collum)
            check(row,collum+1)
            check(row,collum-1)
            check(row-1,collum)
    else:
        return
check (row,collum)




for row in illustration:
    print "".join(row)