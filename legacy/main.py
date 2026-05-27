import sys
    #startup, bases
def legacy():
    run = True
    game = True

    def rajzX(tabla, ui1, ui2):
        tabla[ui1][ui2] = 'X'

    def rajzO(tabla, ui1, ui2):
        tabla[ui1][ui2] = 'O'

    def game_display(board):    
        for sor in range(len(board)):
            for oszlop in range(len(board[sor])):
                if board [sor][oszlop] == None:
                    print('_', end = ' ')
                else:
                    print(board[sor][oszlop], end = ' ')
            print()

    def check_winnerO(board):
        if  ((board[1][1]=='O' and board[1][2]== 'O' and board[1][3]=='O' )or

                (board[2][1]=='O' and board[2][2]=='O' and board[2][3]=='O' )or

                (board[3][1]=='O' and board[3][2]=='O' and board[3][3]=='O' )or

                (board[1][1]=='O' and board[2][1]=='O' and board[3][1]== 'O' )or

                (board[1][2]=='O' and board[2][2]=='O' and board[3][2]=='O' )or

                (board[1][3]=='O' and board[2][3]=='O' and board[3][3]=='O' )or

                (board[1][1]=='O' and board[2][2]=='O' and board[3][3]=='O' )or

                (board[1][3]=='O' and board[2][2]=='O' and board[3][1]=='O' )):
            return True


    def check_winnerX(board):
        if  ((board[1][1]=='X' and board[1][2]== 'X' and board[1][3]=='X' )or

            (board[2][1]=='X' and board[2][2]=='X' and board[2][3]=='X' )or

            (board[3][1]=='X' and board[3][2]=='X' and board[3][3]=='X' )or

            (board[1][1]=='X' and board[2][1]=='X' and board[3][1]== 'X' )or

            (board[1][2]=='X' and board[2][2]=='X' and board[3][2]=='X' )or

            (board[1][3]=='X' and board[2][3]=='X' and board[3][3]=='X' )or

            (board[1][1]=='X' and board[2][2]=='X' and board[3][3]=='X' )or

            (board[1][3]=='X' and board[2][2]=='X' and board[3][1]=='X' )):
            return True

    def check_draw(board):
            szamlalo = 0
            for i in board[1:4]:
                for a in i[1:4]:
                    if a != None:
                        szamlalo += 1
            if szamlalo == 9:
                return True
            else: return False

    def gameend(board, replay):
        if check_winnerX(board) == True:
            print('A játékot P1 nyerte meg.')
            
        elif check_winnerO(board) == True:
            print('A játékot P2 nyerte meg.')
        
        elif check_draw(board) == True:
            print('Döntetlen! Egyik játékos sem nyert!')
        else: return None

        replay = input('Szeretnél tovább játszani?').capitalize()
        if replay == 'I':
            return False
        if replay == 'N':
            return True


        
    # game
    print('Üdvölünk a DBM csapat amőba játékában!')


    #irányítás magyarázat

    #játék
        #játéktábla xx
    tabla = []

    # info_sor = ['', 1, 2 ,3]
    # tabla.append(info_sor)
    # a = ['A', None, None, None]
    # tabla.append(a)
    # b = ['B', None, None, None]
    # tabla.append(b)
    # c = ['C', None, None, None]
    # tabla.append(c)


        #játéktábla használata
    while run:
        info_sor = ['', 1, 2 ,3]
        tabla.append(info_sor)
        a = ['A', None, None, None]
        tabla.append(a)
        b = ['B', None, None, None]
        tabla.append(b)
        c = ['C', None, None, None]
        tabla.append(c)
        x1 = None
        o1 = None
        x2 = None
        o2 = None

        while game:


            print('Az 1. játékos következik')
            x1 = input('Add meg a függőleges kordinációt! (A-C)\n').capitalize()
            if x1 == 'A':
                x1 = 1
            elif x1 == 'B':
                x1 = 2
            elif x1 == 'C':
                x1 = 3
            else:
                print('Nincsen ilyen betükordináció!\n A program el fog törni.')

            x2 = int(input('Add meg a vízszinted kordinációt! (1-3)\n'))   
        #    if x2 != 1 or x2 != 2 or x2 != 3:
        #        print('Nincsen ilyen számkordináció!')

            rajzX(tabla, x1, x2)
            game_display(tabla)
            print(' ')

            regame = None
            useri = gameend(tabla, regame)
            if useri == False:
                tabla.clear()
                game = False
                continue
            elif useri == True:
                sys.exit()


            print('Az 2. játékos következik')
            o1 = input('Add meg a függőleges kordinációt! (A-C)\n').capitalize()
            if o1 == 'A':
                o1 = 1
            elif o1 == 'B':
                o1 = 2
            elif o1 == 'C':
                o1 = 3
            else:
                print('Nincsen ilyen betükordináció! A program el fog törni')

            o2 = int(input('Add meg a vízszinted kordinációt! (1-3)\n'))
        #    if o2 != 1 or o2 != 2 or o2 != 3:
        #        print('Nincsen ilyen számkordináció!')


            rajzO(tabla, o1, o2)

            game_display(tabla)
            print(' ')

            regame = None
            useri = gameend(tabla, regame)
            if useri == False:
                tabla.clear()
                game = False
                continue
            elif useri == True:
                sys.exit()

legacy()