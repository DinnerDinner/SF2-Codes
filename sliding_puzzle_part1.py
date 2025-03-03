#Pranjwal Singh - 2436027
import random
import sys
def tileLabels(n):
    board = []
    for i in range(1, n**2):
        board.append(f'{i} ' if i < 10 else f'{i}')
    board.append('  ')
    return board



def getNewPuzzle(n):
    board = tileLabels(n)
    new_lst = []
    random.shuffle(board)
    for i in range(0, len(board), n):
        new_lst.append(board[i:i+n])
    return new_lst


def findEmptyTile(n):
    board = getNewPuzzle(n)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '  ':
                return (i, j), board
            

def nextMove(n):
    position, board = findEmptyTile(n)
    possible = []
    print(board)
    print(position)
    if position[0]-1>=0:
        possible.append("S")
    if position[0]+1<n:
        possible.append("W")
    if position[1]-1>=0:
        possible.append("D")
    if position[1]+1<n:
        possible.append("A")
    print(possible)
    user = input("Enter WASD (or QUIT): ")
    while user not in possible and user !="quit":
        user = input(" try again: ")

    if user == "quit":
        sys.exit()
    return user

# def displayBoard(board_lst):
#     n = len(board_lst)

#     labels = []
#     for i in range(n):
#         for j in range(n):
#             labels.append(board_lst[i][j])

#     draw_board = ''
#     horizontal_div = ('+' + '------')*n + '+'
#     vertical_div = '|' + ' '*6
#     vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
#     for i in range(n):
#         draw_board = draw_board + horizontal_div +'\n'+\
#                     vertical_div*n + '|\n' + \
#                     vertical_label*n + '|\n'+\
#                     vertical_div*n + '|\n'
#     draw_board += horizontal_div
#     print(draw_board.format(*labels))


            
print(nextMove(3))
