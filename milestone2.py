##### IT'S TIC TAC TOE TIME BABY #####

# GLOBAL VARIABLES #
board = ['PLACEHOLDER', '-', '-', '-', '-', '-', '-', '-', '-', '-']
tag = 'X'
draw = False


# DISPLAY BOARD #
def display():
    print('\n      |' + board[7] + '|' + board[8] + '|' + board[9] + '|     ' + '|7|8|9|')
    print('      |' + board[4] + '|' + board[5] + '|' + board[6] + '|     ' + '|4|5|6|')
    print('      |' + board[1] + '|' + board[2] + '|' + board[3] + '|     ' + '|1|2|3|')


# PLAYER MOVE CHOICE #
def move():

    global board, tag, draw
    display()

    # Player chooses cell
    while True:
        cell = int(input('\n{}, select a cell: '.format(tag)))
        if cell not in range(1,10):
            print('1-9 only please. See legend to the right of the board for cell numbers.')
        elif board[cell] != '-':
            print('Sorry, that spot is taken.')
        else:
            break

    board[cell] = tag

    # Vertical win check
    if board[7] == tag and board[4] == tag and board[1] == tag:
        endgame()
    elif board[8] == tag and board[5] == tag and board[2] == tag:
        endgame()
    elif board[9] == tag and board[6] == tag and board[3] == tag:
        endgame()
    # Horizontal win check
    elif board[7] == tag and board[8] == tag and board[9] == tag:
        endgame()
    elif board[4] == tag and board[5] == tag and board[6] == tag:
        endgame()
    elif board[1] == tag and board[2] == tag and board[3] == tag:
        endgame()
    # Diagonal win check
    elif board[7] == tag and board[5] == tag and board[3] == tag:
        endgame()
    elif board[1] == tag and board[5] == tag and board[9] == tag:
        endgame()
    # Draw check
    elif '-' not in board:
        draw = True
        endgame()
    # Swap who is playing
    else:
        if tag == 'X':
            tag = 'O'
        else:
            tag = 'X'
        move()


# GAME OVER #
def endgame():

    global board, tag
    display()

    # Print win/draw result
    if draw is True:
        print('\nIt\'s a draw!')
    else:
        print('{} wins!'.format(tag))

    # Ask for rematch
    while True:
        rematch = input('Rematch? (y/n) ').lower()
        if rematch == 'y':
            board = ['PLACEHOLDER', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            tag = 'X'
            move()
        elif rematch == 'n':
            print('Thanks for playing!')
            break
        else:
            print('"y" or "n" only please. I am a dumb program. :)')


# IT'S GAME TIME #
move()
