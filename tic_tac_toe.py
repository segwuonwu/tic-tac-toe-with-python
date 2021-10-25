# Game Play 
# Tic-tac-toe is played on a three-by-three grid by 
# two players, who alternately place the marks X and 
# O in one of the nine spaces in the grid.

# Welcome message
def welcome():
    print(
        '''
        WELCOME TO THE GAME OF TIC TAC TOE

        The game is played on a three-by-three grid by two players, who alternately place the marks X and O in one of the nine spaces in the grid.

        Let the game begin 🥁 🥁 🥁
        '''
    )

welcome()

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

# Getting player's input
def player_input():
    player1 = input("Please select a marker 'O or 'X':  \n")
    while True:
        if player1.upper() == 'O':
            player2 = 'X'
            print(f"You picked {player1}. Player 2 will be {player2}")
            return player1.upper(), player2
        elif player1.upper() == 'X':
            player2 = 'O'
            print(f"You picked {player1}. Player 2 will be {player2}")
            return player1.upper(), player2
        else:
            player1 = input("Please select a marker 'O' or 'X':  \n")

player_input()