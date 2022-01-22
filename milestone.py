##### IT'S TIC TAC TOE TIME BABY #####

### GLOBAL VARIABLES
a1 = '-'
a2 = '-'
a3 = '-'
b1 = '-'
b2 = '-'
b3 = '-'
c1 = '-'
c2 = '-'
c3 = '-'
rows = ['a', 'b', 'c']
cols = ['1', '2', '3']
playx = True
playo = False

### DISPLAY BOARD
def display():
    print('')
    print('   1 2 3')
    print('A |' + a1 + '|' + a2 + '|' + a3 + '|')
    print('B |' + b1 + '|' + b2 + '|' + b3 + '|')
    print('C |' + c1 + '|' + c2 + '|' + c3 + '|')
    print('')

### PLAYER MOVE CHOICE
# player X
def movex():
    global playo, playx, a1, a2, a3, b1, b2, b3, c1, c2, c3
    display()
    while playx is True:
# coordinate selection
        x1 = 'DEFAULT'  # row select
        while x1 not in rows:
            x1 = input('Player X, choose a row: ').lower()
            if x1 not in rows:
                print('Sorry, invalid choice.')
        x2 = 'DEFAULT'  # column select
        while x2 not in cols:
            x2 = input('Player X, choose a column: ')
            if x2 not in cols:
                print('Sorry, invalid choice.')
# play commit
        if x1 == 'a':
            if x2 == '1':
                if a1 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    a1 = 'X'
                    playx = False
            elif x2 == '2':
                if a2 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    a2 = 'X'
                    playx = False
            elif x2 == '3':
                if a3 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    a3 = 'X'
                    playx = False
            else:
                print('movex() row A error.')
        elif x1 == 'b':
            if x2 == '1':
                if b1 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    b1 = 'X'
                    playx = False
            elif x2 == '2':
                if b2 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    b2 = 'X'
                    playx = False
            elif x2 == '3':
                if b3 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    b3 = 'X'
                    playx = False
            else:
                print('movex() row B error.')
        elif x1 == 'c':
            if x2 == '1':
                if c1 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    c1 = 'X'
                    playx = False
            elif x2 == '2':
                if c2 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    c2 = 'X'
                    playx = False
            elif x2 == '3':
                if c3 != '-':
                    print('That spot is already taken.')
                    movex()
                else:
                    c3 = 'X'
                    playx = False
            else:
                print('movex() row C error.')
        else:
            print('Play commit error.')
    playo = True
    win_check()

# player O
def moveo():
    global playo, playx, a1, a2, a3, b1, b2, b3, c1, c2, c3
    display()
    while playo is True:
# coordinate selection
        o1 = 'DEFAULT'  # row select
        while o1 not in rows:
            o1 = input('Player O, choose a row: ').lower()
            if o1 not in rows:
                print('Sorry, invalid choice.')
        o2 = 'DEFAULT'  # column select
        while o2 not in cols:
            o2 = input('Player O, choose a column: ')
            if o2 not in cols:
                print('Sorry, invalid choice.')
# play commit
        if o1 == 'a':
            if o2 == '1':
                if a1 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    a1 = 'O'
                    playo = False
            elif o2 == '2':
                if a2 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    a2 = 'O'
                    playo = False
            elif o2 == '3':
                if a3 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    a3 = 'O'
                    playo = False
            else:
                print('moveo() row A error.')
        elif o1 == 'b':
            if o2 == '1':
                if b1 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    b1 = 'O'
                    playo = False
            elif o2 == '2':
                if b2 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    b2 = 'O'
                    playo = False
            elif o2 == '3':
                if b3 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    b3 = 'O'
                    playo = False
            else:
                print('moveo() row B error.')
        elif o1 == 'c':
            if o2 == '1':
                if c1 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    c1 = 'O'
                    playo = False
            elif o2 == '2':
                if c2 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    c2 = 'O'
                    playo = False
            elif o2 == '3':
                if c3 != '-':
                    print('That spot is already taken.')
                    moveo()
                else:
                    c3 = 'O'
                    playo = False
            else:
                print('moveo() row C error.')
        else:
            print('Play commit error.')
    playx = True
    win_check()

### WIN CHECK BETWEEN TURNS
def win_check():
    global playo, playx, a1, a2, a3, b1, b2, b3, c1, c2, c3
# columns
    if a1 == 'X' and b1 == 'X' and c1 == 'X' or a1 == 'O' and b1 == 'O' and c1 == 'O':
        if a1 == 'X':
            xwin()
        elif a1 == 'O':
            owin()
    elif a2 == 'X' and b2 == 'X' and c2 == 'X' or a2 == 'O' and b2 == 'O' and c2 == 'O':
        if a2 == 'X':
            xwin()
        elif a2 == 'O':
            owin()
    elif a3 == 'X' and b3 == 'X' and c3 == 'X' or a3 == 'O' and b3 == 'O' and c3 == 'O':
        if a3 == 'X':
            xwin()
        elif a3 == 'O':
            owin()
# rows
    elif a1 == 'X' and a2 == 'X' and a3 == 'X' or a1 == 'O' and a2 == 'O' and a3 == 'O':
        if a1 == 'X':
            xwin()
        elif a1 == 'O':
            owin()
    elif b1 == 'X' and b2 == 'X' and b3 == 'X' or b1 == 'O' and b2 == 'O' and b3 == 'O':
        if b1 == 'X':
            xwin()
        elif b1 == 'O':
            owin()
    elif c1 == 'X' and c2 == 'X' and c3 == 'X' or c1 == 'O' and c2 == 'O' and c3 == 'O':
        if c1 == 'X':
            xwin()
        elif c1 == 'O':
            owin()
# diagonals
    elif a1 == 'X' and b2 == 'X' and c3 == 'X' or a1 == 'O' and b2 == 'O' and c3 == 'O':
        if a1 == 'X':
            xwin()
        elif a1 == 'O':
            owin()
    elif c1== 'X' and b2 == 'X' and a3 == 'X' or c1 == 'O' and b2 == 'O' and a3 == 'O':
        if c1 == 'X':
            xwin()
        elif c1 == 'O':
            owin()
# draw
    elif a1 != '-' and a2 != '-' and a3 != '-' and b1 != '-' and b2 != '-' and b3 != '-' and c1 != '-' and c2 != '-' and c3 != '-':
        display()
        print('It\'s a draw!')
        i = ['y', 'n']
        rematch = 'DEFAULT'
        while rematch not in i:
            rematch = input('Play again? (y/n) ').lower()
            if rematch not in i:
                print('"y" or "n" please. I am a dumb program. :)')
        if rematch == 'y':
            a1 = '-'
            a2 = '-'
            a3 = '-'
            b1 = '-'
            b2 = '-'
            b3 = '-'
            c1 = '-'
            c2 = '-'
            c3 = '-'
            playx = True
            playo = False
            movex()
        elif rematch == 'n':
            playx = False
            playo = False
            print('Thanks for playing!')
        else:
            print('win_check() draw error.')
    else:
        turn()

# X or O finished turn
def turn():
    if playx is True:
        movex()
    elif playo is True:
        moveo()
    else:
        pass

# X wins, ask for rematch
def xwin():
    global playo, playx, a1, a2, a3, b1, b2, b3, c1, c2, c3
    display()
    print('X wins!')
    i = ['y', 'n']
    rematch = 'DEFAULT'
    while rematch not in i:
        rematch = input('Play again? (y/n) ').lower()
        if rematch not in i:
            print('"y" or "n" please. I am a dumb program. :)')
    if rematch == 'y':
        a1 = '-'
        a2 = '-'
        a3 = '-'
        b1 = '-'
        b2 = '-'
        b3 = '-'
        c1 = '-'
        c2 = '-'
        c3 = '-'
        playx = True
        playo = False
        movex()
    elif rematch == 'n':
        playx = False
        playo = False
        print('Thanks for playing!')
    else:
        print('xwin() error.')

# O wins, ask for rematch
def owin():
    global playo, playx, a1, a2, a3, b1, b2, b3, c1, c2, c3
    display()
    print('O wins!')
    i = ['y', 'n']
    rematch = 'DEFAULT'
    while rematch not in i:
        rematch = input('Play again? (y/n) ').lower()
        if rematch not in i:
            print('"y" or "n" please. I am a dumb program. :)')
    if rematch == 'y':
        a1 = '-'
        a2 = '-'
        a3 = '-'
        b1 = '-'
        b2 = '-'
        b3 = '-'
        c1 = '-'
        c2 = '-'
        c3 = '-'
        playx = True
        playo = False
        movex()
    elif rematch == 'n':
        playx = False
        playo = False
        print('Thanks for playing!')
    else:
        print('owin() error.')

# Let the game begin!
movex()
