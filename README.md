from random import randint

board = []

def creating_board():

    row = input("Give the number of rows: ")
    col = input("Give the number of columns: ")

    for i in range(int(row)):
        rows = []
        board.append(rows)
        for j in range(int(col)):
            rows.append("SEA|")
    for rows in board:
        print("".join(rows))

    x = randint(0,int(row) - 1)
    y = randint(0,int(col) - 1)
    
    ship = "SHP|"
    board[int(x)][int(y)] = ship
   
def targeting():

    turn = 0

    while turn <=5:
        turn += 1
        x = input("Give the 'x' coordinate: ")
        y = input("Give the 'y' coordinate: ")

        if board[int(x) - 1][int(y) - 1] == "SHP|":
            print("hit")
            board[int(x) - 1][int(y) - 1] = "HIT|"
            for rows in board:
                print("".join(rows))
            break
        else:
            print("miss")
            board[int(x) - 1][int(y) - 1] = "MIS|"
            for rows in board:
                print("".join(rows))

creating_board()
targeting()
