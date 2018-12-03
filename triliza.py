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
