# Game Play 
# Tic-tac-toe is played on a three-by-three grid by 
# two players, who alternately place the marks X and 
# O in one of the nine spaces in the grid.

# Create a display board
def display_board(board):
    blank_board = '''
    |-----------------------|
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    |-----------------------|
    |       |       |       |
    |   4   |   5   |   6   |
    |       |       |       |
    |-----------------------|
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    |-----------------------|
    '''

    for i in range(1,10):
        if(board[i] == 'O' or board[i] == 'X'):
            blank_board = blank_board.replace(str(i), board[i])
        else:
            blank_board = blank_board.replace(str(i), " ")
    print(blank_board)

board = ['#','#','#','#','#','#','#','#','#','#']
display_board(board)