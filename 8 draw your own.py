__author__ = 'macuser'
illustration = []
row_counter = 0
#make lits of lists
with open("map.txt", "r") as map:
    for line in map:
        illustration.append([])
        row_counter = row_counter + 1
        for character in line:
            if character != '\n':
                illustration[-1].append(character)
print len(line)
print row_counter

row_start_point = row_counter + 1
collum_start_point = len(line) + 1



while row_start_point < -1 or row_start_point > row_counter-1:
    row_start_point = int(raw_input("What row to start in(0 to %s)" %(row_counter-1)))

while collum_start_point < -1 or collum_start_point > len(line)-1:
    collum_start_point = int(raw_input("What collum to start in(0 to %s)" %(len(line)-1)))

row = row_start_point
collum = collum_start_point

while illustration[row][collum] == "X":
    row = row + 1
    print "loop"

def check(row,collum):
    if row < row_counter and collum < len(line) and row > -1 and collum > -1:
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