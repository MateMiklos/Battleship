board = []

def creating_board():

    rows = []

    row = input("Give the number of rows: ")
    col = input("Give the number of columns: ")

    for i in range(int(row)):
        board.append(rows)
    for j in range(int(col)):
        rows.append("SEA|")
    for rows in board:
        print("".join(rows))

def placing_ships():
    
    x = input("Give the 'x' coordinate: ")
    y = input("Give the 'y' coordinate: ")

    ship = "SHP|"
    board[int(x)][int(y)] = ship

def targeting():

    while True:
        x = input("Give the 'x' coordinate: ")
        y = input("Give the 'y' coordinate: ")

        if board[int(x)][int(y)] == "SHP|":
            print("hit")
            board[int(x)][int(y)] = "HIT|"
            for rows in board:
                print("".join(rows))
            break
        else:
            print("miss")
            board[int(x)][int(y)] = "MIS|"
            for rows in board:
                print("".join(rows))

creating_board()
placing_ships()
targeting()
print(board)
