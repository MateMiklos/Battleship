from random import randint

l = []
turn = 0

size = input("Give the size of the sea: ")
turns = input("Give how many turns do you need: ")
print("LET DA BATTLE BEGIN, YA LAND LUBBER!!!")

for x in range(int(size)):
    l.append(['\x1b[0;37;44m' + 'SEA|' + '\x1b[0m'] * int(size))

for i in l: 
    print(*i)

row = randint(0, int(size) - 1)
col = randint(0, len(l[0]) - 1)
print(row + 1, col + 1)

while turn < int(turns):
    r = int(input("ROW: "))
    c = int(input("COL: "))
    if int(r) - 1 == row and int(c) - 1 == col:
        l[int(row)][int(col)] = "SHP|"
        print('\x1b[6;30;42m' + 'HIT! DAMN IT! YOU SANK MY SHIP!' + '\x1b[0m')
        print('\x1b[6;30;42m' + 'CONGRATS! YOU WON! YOU DESERVE A RUM!' + '\x1b[0m')
        l[int(row2)][int(col)] = ('\x1b[6;30;42m' + 'HIT|' + '\x1b[0m')
        for i in l:
            print(*i)
        break
    else:
        print('\x1b[0;37;41m' + 'MISS! TRY AGAIN!' + '\x1b[0m')
        print(r,c , row , col)
        l[int(r) - 1][int(c) - 1] = '\x1b[0;37;41m' + '_X_|' + '\x1b[0m'
        for i in l:
            print((" ").join(i))
        turn += 1
        if turn == int(turns):
            print('\x1b[0;37;41m' + 'MISS! I EXPECTED MORE, LOSER!' + '\x1b[0m!')
            l[row][col] = '\x1b[1;30;47m' + 'SHP|' + '\x1b[0m'
            print("Exit")
            break
