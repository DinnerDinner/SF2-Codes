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
    return findEmptyTile(132)



def findEmptyTile():
    for i in range(len(board_lst)):
        for j in range(len(board_lst[i])):
            if board_lst[i][j] == '  ':
                return (i, j)
            
def nextMove():
    position = findEmptyTile()
    possible = []
    if position[1]+1<len(board_lst):
        possible.append("A")
    if position[0]-1>=0:
        possible.append("S")
    if position[0]+1<len(board_lst):
        possible.append("W")
    if position[1]-1>=0:
        possible.append("D")

    first_line = f'\t\t\t {"(W)" if "W" in possible else "(  )"}'
    second_line = 'Enter WASD (or QUIT):' + " ".join(f'({m})' if m in possible else '(  )' for m in ["A", "S", "D"])
    user = input(f"{first_line}\n{second_line}\n>")
    
    while user not in possible and user.lower() !="quit":
        user = input(f"{first_line}\n{second_line}\n>")

    if user == "quit":
        sys.exit()
    return user

board_lst = getNewPuzzle(3)
print(nextMove())

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


        

