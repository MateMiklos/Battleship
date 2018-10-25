from random import randint

turn = 0
l = []

for x in range(5):
    l.append(["SEA|"] * 5)

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
    if r == row2 and c == col:
        print("HIT! YOU SANK MY SHIP!")
        break
    elif turn == 5:
        print("MISS! LOSER!")
        l[row2][col] = "SHP|"
        print("Exit")
        break
    else:
        print("MISS! TRY AGAIN!")
        print(r,c , row2 , col)
        l[int(r)][int(c)] = "XXX|"
        for row in l:
            print((" ").join(row))
        turn += 1
