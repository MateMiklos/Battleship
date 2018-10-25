from random import randint


l = []
turn = 0
size = input("Give the size of the sea: ")
turns = input("Give how many turns do you need: ")
print("LET DA BATTLE BEGIN, YA LAND LUBBER!!!")


for x in range(int(size)):
    l.append(['\x1b[0;37;44m' + 'SEA|' + '\x1b[0m'] * int(size))

for row in l: 
    print(*row)


row2 = randint(0, int(size) - 1)
col = randint(0, len(l[0]) - 1)
#print(row2, col)


while turn < int(turns):
    r = int(input("ROW: "))
    c = int(input("COL: "))
    if int(r) - 1 == row2 and int(c) - 1 == col:
        l[int(row2)][int(col)] = "SHP|"
        print("HIT! YOU SANK MY SHIP!")
        for row in l:
            print((" ").join(row))
        break
    else:
        print("HA-HA-HA! MISS! TRY AGAIN!")
        print(r,c , row2 , col)
        l[int(r) - 1][int(c) - 1] = "XXX|"
        for row in l:
            print((" ").join(row))
        turn += 1
        if turn == int(turns):
            print("MISS! I EXPECTED MORE, LOSER!")
            l[row2][col] = "SHP|"
            print("Exit")
            break
