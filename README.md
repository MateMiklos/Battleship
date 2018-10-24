import copy
import random
horiz = ['  A  ','  B  ','  C  ','  D  ','  E  ','  F  ','  G  ','  H  ','  I  ','  J  ','  K  ']
str1 = ''.join(horiz)
vert = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
board_size = int(input("What size of game board? "))
def print_horiz_line():
    print(" ___ " * board_size)
def print_vert_line():
    print("|    " * (board_size + 1))
print(str1[:board_size * 5])
#print(vert[:board_size])
for index in range(board_size):
    print_horiz_line()
    print_vert_line()
print_horiz_line()
