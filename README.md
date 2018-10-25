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
    if int(r) -1 == row2 and int(c) -1 == col:
        l[int(row2)][int(col)] = "SHP|"
        print("HIT! YOU SANK MY SHIP!")
        for row in l:
            print((" ").join(row))
        break
    elif turn == 5:
        print("MISS! LOSER!")
        l[row][col] = "SHP|"
        print("Exit")
        break
    else:
        print("MISS! TRY AGAIN!")
        l[int(r) -1][int(c) -1] = "XXX|"
        for row in l:
            print((" ").join(row))
        turn += 1
        
