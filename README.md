from random import randint

turn = 0
l = []

for x in range(5):
    l.append(['\x1b[0;37;44m' + 'SEA|' + '\x1b[0m'] * 5)

def grid(l):
    for row in l: 
        print((" ").join(row))
grid(l)

row2 = randint(0, 4)
col = randint(0, len(l[0]) - 1)
print(row2, col)

while turn <= 5:
    r = int(input("ROW: "))
    c = int(input("COL: "))
    if int(r) -1 == row2 and int(c) -1 == col:
        print('\x1b[6;30;42m' + 'HIT! YOU SANK MY SHIP!' + '\x1b[0m')
        print('\x1b[6;30;42m' + 'CONGRATS! YOU WON!' + '\x1b[0m')
        l[int(row2)][int(col)] = ('\x1b[6;30;42m' + 'HIT|' + '\x1b[0m')
        for row in l:
            print((" ").join(row))
        print("Exit")
        break
    elif turn == 5:
        print('\x1b[0;37;41m' + 'MISS! LOSER!' + '\x1b[0m')
        l[int(row2)][int(col)] = ('\x1b[1;30;47m' + 'SHP|' + '\x1b[0m')
        for row2 in l: 
            print((" ").join(row2))
        print("Exit")
        break
    else:
        print('\x1b[0;37;41m' + 'MISS! TRY AGAIN!' + '\x1b[0m')
        l[int(r) - 1][int(c) - 1] = ('\x1b[0;37;41m' + '_X_|' + '\x1b[0m')
        for row in l:
            print((" ").join(row))
        turn += 1
