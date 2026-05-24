from blessed import Terminal
term= Terminal()
import time
import random
import pygame
import io

pygame.mixer.init()

highlight = pygame.mixer.Sound(f"sfx/key_press.mp3")
challange = False
def typewriter(text, delay=0.04,):
    
    for i in text:
        print(i, end="", flush=True)
        if random.randint(0,1)==1:
            highlight.play()
        time.sleep(delay)
    time.sleep(1)
""" def drunk_typewriter(text, delay=0.1):
    for i in text:
        print(f"{i}{" "*random.randint(0,2)}", end="", flush=True)
        time.sleep(delay) """

def transition(sleep=0.1):
    with term.hidden_cursor():
        temp=list(range(term.height))
        random.shuffle(temp)
        for i in temp:
            with term.location(0, i):
                print("█"*term.width, end="", flush=False)
                time.sleep(sleep)
def cell(x, y, color, term):
    with term.location(x-2, y):
        print(color + "═════" + term.normal)
    with term.location(x-2, y+2):
        print(color + "═════" + term.normal)
    with term.location(x-3, y+1):
        print(color + "║" + term.normal)
    with term.location(x+3, y+1):
        print(color + "║" + term.normal)
    with term.location(x+3, y):
        print(color + "╗" + term.normal)
    with term.location(x-3, y):
        print(color + "╔" + term.normal)
    with term.location(x+3, y+2):
        print(color + "╝" + term.normal)
    with term.location(x-3, y+2):
        print(color + "╚" + term.normal)

def actIprologe():
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        
        with term.location(0, 0):
            typewriter("MEANWHILE: Somwhere at a bar....\n")
            print("="*40)
            typewriter("[ALC-001]: Do you think you can just... *hic* ...walk in here and expect me to give it to you\n")
            typewriter("[ALC-001]: I like it when it is a little more challanging\n")
            while True:
                print(f"\r{term.yellow}press [ENTER] to challange him{term.normal}", end="")
                if term.inkey(timeout=0.5).name=="KEY_ENTER":
                    break
                print(f"\r{" "*40}", end="")
                if term.inkey(timeout=0.5).name=="KEY_ENTER":
                    break
            print(f"\r{term.color(94)}{term.ljust('You have challanged him!')}{term.normal}")
            typewriter("[ALC-001]: Yeah, that's right! A duel of.... *hic* ....wits! Wait, what game are we playing again?\n")
            time.sleep(1.5)
        transition()
            
def actI():
    tes = "X"
    x=int(term.width/2)
    y=3
    line_num = 0
    following = True
    pos=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]
    row=0
    col=0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            
            board = f"""\
     a     b     c   
  ╔═════╦═════╦═════╗
  ║  {pos[0][0]}  ║  {pos[0][1]}  ║  {pos[0][2]}  ║
  ╠═════╬═════╬═════╣
  ║  {pos[1][0]}  ║  {pos[1][1]}  ║  {pos[1][2]}  ║
  ╠═════╬═════╬═════╣
  ║  {pos[2][0]}  ║  {pos[2][1]}  ║  {pos[2][2]}  ║
  ╚═════╩═════╩═════╝
    """
            
            board = io.StringIO(board)
            for i in board:
                with term.location(int((term.width/2)-len(i)/2), line_num+2):
                    print(i, end="")
                    line_num= line_num+1
            line_num=0
            board.seek(0)
            cell(x, y, term.red, term)
            key = term.inkey()

            with term.location(x, y+1):
                print(" ", end="")

            if key.name == "KEY_ESCAPE" or key == "q":
                return
            if key == "n":
                pygame.mixer.music.stop()


            if True:
            
                
                
                if key == "w" or key.name == "KEY_UP":
                    y = y - 2

                if key == "s" or key.name == "KEY_DOWN":
                    y = y + 2

                if key == "d" or key.name == "KEY_RIGHT":
                    x = x + 6

                if key == "a" or key.name == "KEY_LEFT":
                    x = x - 6

                if x > int(term.width/2)+7:
                    x = x - 6

                if x < int(term.width/2)-7:
                    x = x + 6

                if y > 8:
                    y = y - 2

                if y < 3:
                    y = y + 2
                
            if x==int((term.width/2)-6):
                col=0
            if x==int((term.width/2)):
                col=1
            if x==int((term.width/2)+6):
                col=2
            if y==3:
                row=0
            if y==5:
                row=1
            if y==7:
                row=2
            with term.location(0,0):
                print(col, row)
            with term.location(0,1):
                print(x, y)
                
                if key.name == "KEY_ENTER" or key==" ":
                    if following and pos[row][col]==" ":
                        pos[row][col]="X"
                        following = not following
                    while not following:
                        temp=0
                        for i in pos:
                            for a in i:
                                if a!=" ":
                                    temp+=1
                        if temp!=9:
                            rand_1=random.randint(0, 2)
                            rand_2=random.randint(0, 2)
                            if pos[rand_1][rand_2]==" ":
                                pos[rand_1][rand_2]="O"
                                following = not following
                        else:
                            break
                            
                            
                    for i in range(0, 2):
                        if pos[i][0]==pos[i][1]==pos[i][2]=="X":
                            with term.location(0,3):
                                print("X won")
                        if pos[i][0]==pos[i][1]==pos[i][2]=="O":
                            with term.location(0,3):
                                print("O won")
                        if pos[0][i]==pos[1][i]==pos[2][i]=="X":
                            with term.location(0,3):
                                print("X won")
                        if pos[0][i]==pos[1][i]==pos[2][i]=="O":
                            with term.location(0,3):
                                print("O won")
                        if pos[0][0]==pos[1][1]==pos[2][2]=="X":
                            with term.location(0,3):
                                print("X won")
                        if pos[2][0]==pos[1][1]==pos[0][2]=="X":
                            with term.location(0,3):
                                print("X won")
                        if pos[0][0]==pos[1][1]==pos[2][2]=="O":
                            with term.location(0,3):
                                print("O won")
                        if pos[2][0]==pos[1][1]==pos[0][2]=="O":
                            with term.location(0,3):
                                print("O won")
                    if temp==9:
                        with term.location(0,3):
                            print("draw")



actI()