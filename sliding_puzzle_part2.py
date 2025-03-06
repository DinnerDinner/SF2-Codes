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

def findEmptyTile(board_lst):
    for i in range(len(board_lst)):
        for j in range(len(board_lst[i])):
            if board_lst[i][j] == '  ':
                return (i, j)
                      
def nextMove(position, board_lst):
    possible = []
    if position[1]+1<len(board_lst):
        possible.append("A")
    if position[0]-1>=0:
        possible.append("S")
    if position[0]+1<len(board_lst):
        possible.append("W")
    if position[1]-1>=0:
        possible.append("D")
    displayBoard(board_lst)
    first_line = f'\t\t\t {"(W)" if "W" in possible else "(  )"}'
    second_line = 'Enter WASD (or QUIT):' + " ".join(f'({m})' if m in possible else '(  )' for m in ["A", "S", "D"])
    user = input(f"{first_line}\n{second_line}\n>")
    
    while user not in possible and user.lower() !="quit":
        print("Invalid move. Try again!")
        user = input(f"{first_line}\n{second_line}\n>")

    if user == "quit":
        sys.exit()
    return user
        
def makeMove(board, move):
    position = findEmptyTile(board)
    x, y = position[0], position[1]
    if move == "W": 
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
    elif move == "S": 
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
    elif move == "A": 
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
    elif move == "D":
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
    return board

def displayBoard(board_lst):
    n = len(board_lst)
    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def main():
    print("Hi!!! Welcome to the sliding puzzle! Slide about the tiles with W, S, A, D \n \
          The player wins when all the numbered tiles are arranged in the correct order, with the empty space in the bottom-right corner!")
    dimension = int(input("Board Dimension?> "))

    board = getNewPuzzle(dimension)
    solved = []
    
    for i in range(1, len(board)**2):
        solved.append(f'{i} ' if i < 10 else f'{i}')
    solved.append('  ')
    max_moves = {3: 31, 4: 80}
    max_moves[len(board)] = max_moves.get(len(board), len(board)**4) #honestly just needed to deal with in case they input something like 2 or 4
    num_moves = 1
    
    while [item for sublist in board for item in sublist] != solved and num_moves<=max_moves[len(board)]:
        position = findEmptyTile(board)
        user_move = nextMove(position, board)
        board = makeMove(board, user_move)
        num_moves+=1
    displayBoard(board)
    return "Congratulations!! YOU WIN; Here's a candy 🍬!" if [item for sublist in board for item in sublist] == solved else "Best of luck next time!"
    
# print(main())