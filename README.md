from random import randint

l = []

for x in range(5):
    l.append(["SEA|"] * 5)

def grid(l):
    for row in l: 
        print((" ").join(row))
grid(l)

row = randint(0, 4)
col = randint(0, len(l[0]) - 1)
print(row, col)

for i in range(4):
    r = int(input("ROW: "))
    c = int(input("COL: "))
    if r == row and c == col:
        print("HIT! YOU SANK MY SHIP!")
        break
    else:
        print("MISS! TRY AGAIN!")
        l[int(r)][int(c)] = "XXX|"
        for row in l:
            print((" ").join(row))
        
for i in range(1):
    r = int(input("ROW: "))
    c = int(input("COL: "))
    if r == row and c == col:
        print("HIT! YOU SANK MY SHIP!")
        l[int(r)][int(c)] = "HIT|"
        break
    else:
        print("MISS! LOSER!")
        l[row][col] = "SHP|"
        print("Exit")
        break
