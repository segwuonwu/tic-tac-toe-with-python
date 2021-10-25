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

#player_input()

# Placing the markers on the board
def place_marker(board, marker, position):
    board[position] = marker
    return board

# Check if the position is empty and place player's marker
def check_space(board, position):
    return board[position] == '#'

def player_position(board):
    position = input("Please select an empty position between 1 and 9 \n")
    while not check_space(board, int(position)):
        position = input('This position is not empty. \nPlease try another position between 1 and 9 : \n')
    return int(position)

# Check to see if the board is full
def is_board_full(board):
    return len([x for x in board if x == '#']) == 1

# Check if the game has been won
def check_win(board, marker):
    if board[1] == board[2] == board[3] == marker:
            return True
    if board[4] == board[5] == board[6] == marker:
        return True
    if board[7] == board[8] == board[9] == marker:
        return True
    if board[1] == board[4] == board[7] == marker:
        return True
    if board[2] == board[5] == board[8] == marker:
        return True
    if board[3] == board[6] == board[9] == marker:
        return True
    if board[1] == board[5] == board[9] == marker:
        return True
    if board[3] == board[5] == board[7] == marker:
        return True
    return False

# Ask player if they want to play again
def play_again():
    replay = input("Would you like to play again (y/n) ? \n")
    if replay.lower() == 'y':
        return True
    if replay.lower() == 'n':
        return False

player1, player2 = player_input()
position = player_position(board)
marker = place_marker(board, player1, position)
print(marker)
display_board(board)