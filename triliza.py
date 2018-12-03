from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('  |   |')
    print(' '+ board[1]+'| '+ board[2] +' | '+ board[3])
    print('  |   |')
    print('---------')
    print('  |   |')
    print(' '+ board[4]+'| '+ board[5] +' | '+ board[6])
    print('  |   |')
    print('---------')
    print('  |   |')
    print(' '+ board[7]+'| '+ board[8] +' | '+ board[9])
    print('  |   |')

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while marker !='X' and marker !='O':
        marker = input('Player 1 Choose X or O: ').upper()
        if marker == 'X':
            return ('X','O')
        else :
            return ('O','X')

import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def place_marker (board,marker,position):
    board[position] = marker

def win_check(board,mark):
    # check rows,columns and diagonal
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark)) 

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    # Board is full when return True
    return True

def player_choise(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position 1-9 '))
    return position

def replay():
    choise = input('Play again? Enter Yes or No')
    return choise == 'Yes'

print('Welcome to Tic Tac Toe')

while True:
    ##Play the Game
    
    ###set everything up
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? yes or no? ')
    
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False
        
    ###Game Play
    while game_on:
        if turn == 'Player 1' :
            #show the board
            display_board(the_board)
            #Choose a positiom
            position = player_choise(the_board)
            #Place the msrker on the position
            place_marker(the_board,player1_marker,position)
            
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Playr 1 won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 2'
            
        else:
                #show the board
                display_board(the_board)
                #Choose a positiom
                position = player_choise(the_board)
                #Place the msrker on the position
                place_marker(the_board,player2_marker,position)
            
                #check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('Playr 2 won!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie Game!')
                        break
                    else:
                        turn = 'Player 1'
    
    if not replay():
        break

