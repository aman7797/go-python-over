from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + '   |' + board[8] + '   |' + board[9])
    print('--------------')
    print(board[4] + '   |' + board[5] + '   |' + board[6])
    print('--------------')
    print(board[1] + '   |' + board[2] + '   |' + board[3])
    
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O:')
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def place_marker(board, marker, position):
    
    board[position] = marker
    return board
    
def win_check(board, mark):
    
    # Win Game
    return ((board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or (board[1] == board[2] == board[3] == mark) or # accross row
    (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark) or # across column
    (board[7] == board[5] == board[3] == mark) or (board[9] == board[5] == board[1] == mark)) # diagonal

import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    
    return board[position] == ' '
        
def full_board_check(board):
    return board.count(' ') >= 2
    
def player_choice(board):
    
#     position = 0
#     while position not in [1,2,3,4,5,6,7,8,9] or space_check(board,position):
#         position = int(input('Chose a position: (1-9) ::'))
    valid_input = True
    
    while valid_input:
        position = int(input('Chose a position: (1-9) ::'))
        if space_check(board,position) and position in [1,2,3,4,5,6,7,8,9]:
            valid_input = False
        else :
            print('-------------  Please select empty postion  -------------')
        
    
    return position

def replay():
    
    choice = input("Play again? Enter Y or N :: ")
    return choice.upper(  ) == 'Y'

##### print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            
            place_marker(theBoard, player1_marker, position)
            
            display_board(theBoard)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    turn = 'Player 2'
                else:
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                    

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    turn = 'Player 1'
                else:
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                    

    if not replay():
        break