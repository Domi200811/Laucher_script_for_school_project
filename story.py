from blessed import Terminal

term = Terminal()
import time
import random
import pygame
import io
import sys

pygame.mixer.init()

highlight = pygame.mixer.Sound(f"sfx/key_press.mp3")
highlight.set_volume(0.7)
challange = False

def typewriter(
    text,
    delay=0.04,
):

    for i in text:
        print(i, end="", flush=True)
        if random.randint(0, 1) == 1:
            highlight.play()
        time.sleep(delay)
    time.sleep(1)


""" def drunk_typewriter(text, delay=0.1):
    for i in text:
        print(f"{i}{" "*random.randint(0,2)}", end="", flush=True)
        time.sleep(delay) """


def transition(sleep=0.1):
    with term.hidden_cursor():
        temp = list(range(15))
        random.shuffle(temp)
        for i in temp:
            with term.location(0, i):
                print("█" * term.width, end="", flush=False)
                time.sleep(sleep)

def intro():
    term = Terminal()
    line_num=0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        time.sleep(1.5)
        pygame.mixer.Sound(f"sfx/cinematic-logo.mp3").play()
        # 1. Define the grayscale color codes for 256-color terminals.
        # In the 256-color palette, codes 232 to 255 are a clean gradient from dark gray to near-white.
        # We include '15' at the end for pure brilliant white.
        grayscale_palette = [16, 16, 16] + list(range(232, 256)) + [15]
        
        
        logo=None
        # 2. Loop through the colors to create the brightening effect
        with open("ASCII/LOGO.TXT", encoding="utf-8") as f:
            logo=f.readlines()
        for color_code in grayscale_palette:
        # Move cursor to home (0,0) so we overwrite the same line safely
        
            for i in logo:
                with term.location(int((term.width/2)-len(i)/2), line_num):
                    print(term.color(color_code) + i + term.normal, end='', flush=True)
                    line_num+=1
            line_num=0
        # Adjust this sleep timer to make the fade faster or slower
            time.sleep(0.1)
            
        time.sleep(5)

def cell(x, y, color, term):
    with term.location(x - 2, y):
        print(color + "═════" + term.normal)
    with term.location(x - 2, y + 2):
        print(color + "═════" + term.normal)
    with term.location(x - 3, y + 1):
        print(color + "║" + term.normal)
    with term.location(x + 3, y + 1):
        print(color + "║" + term.normal)
    with term.location(x + 3, y):
        print(color + "╗" + term.normal)
    with term.location(x - 3, y):
        print(color + "╔" + term.normal)
    with term.location(x + 3, y + 2):
        print(color + "╝" + term.normal)
    with term.location(x - 3, y + 2):
        print(color + "╚" + term.normal)

def board(pos):
    board = f"""
  ╔═════╦═════╦═════╗
  ║  {pos[0][0]}  ║  {pos[0][1]}  ║  {pos[0][2]}  ║
  ╠═════╬═════╬═════╣
  ║  {pos[1][0]}  ║  {pos[1][1]}  ║  {pos[1][2]}  ║
  ╠═════╬═════╬═════╣
  ║  {pos[2][0]}  ║  {pos[2][1]}  ║  {pos[2][2]}  ║
  ╚═════╩═════╩═════╝"""

    board = io.StringIO(board)
    line_num = 0
    for i in board:
        with term.location(int((term.width / 2) - 11), line_num + 2):
            print(i, end="")
            line_num = line_num + 1
    board.seek(0)

def win_check(pos, who):
    for i in range(0, 3):
        if pos[i][0] == pos[i][1] == pos[i][2] and who in pos[i][0]:
            return True
        if pos[0][i] == pos[1][i] == pos[2][i] and who in pos[0][i]:
            return True
    if pos[0][0] == pos[1][1] == pos[2][2] and who in pos[1][1]:
        return True
    if pos[2][0] == pos[1][1] == pos[0][2] and who in pos[1][1]:
        return True

def actIprologe():
    pygame.mixer.music.load(f"story_music/Dark Night.mp3")
    pygame.mixer.music.play()
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():

        with term.location(0, 0):
            typewriter("MEANWHILE: Somwhere at a bar....\n")
            print("=" * 40)
            typewriter(
                "[ALC-001]: Do you think you can just... *hic* ...walk in here and expect me to give it to you?!\n"
            )
            typewriter("[ALC-001]: I like it when it is a little more challanging\n")
            while True:
                print(
                    f"\r{term.yellow}press [ENTER] to challange him{term.normal}",
                    end="",
                )
                if term.inkey(timeout=0.5).name == "KEY_ENTER":
                    break
                print(f"\r{" "*40}", end="")
                if term.inkey(timeout=0.5).name == "KEY_ENTER":
                    break
            print(
                f"\r{term.color(94)}{term.ljust('You have challanged him!')}{term.normal}"
            )
            typewriter(
                "[ALC-001]: Yeah, that's right! A duel of.... *hic* ....wits! Wait, what game are we playing again?\n"
            )
            
            time.sleep(1.5)
            pygame.mixer.music.fadeout(1500)
            pygame.mixer.music.load(f"story_music/Dropkick Murphys - I'm Shipping Up to Boston (Instrumental).mp3")
            pygame.mixer.music.play(loops=-1, fade_ms=2000)
        transition()


def actI():
    tes = "X"
    x = int(term.width / 2)
    y = 3
    line_num = 0
    won=False
    following = True
    pos = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    row = 0
    col = 0
    x_won = False
    o_won = False
    tie = False
    voice_line = [
    "That's your move? Ha! I've seen better strategy from a spilled beer.",
    "Hold on, let me take a sip before I crush your hopes... *gulp*",
    "Is the board spinning for you too, or is it just me? *hic*",
    "Whatever. My turn. Watch and learn how a real master plays.",
    "Wait... *hic*... you think I don't see what you're doing there?",
    "Hey! Stop looking at my side of the board! *hic*",
    "I'm drunk and even I know that was a terrible option.",
    "*rubs his eyes*... I swear one of these lines just blinked at me.",
    "*aggressively slams his empty glass onto the wooden table*",
]
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with term.location(0, 2):
            print("="*term.width,end="")
        with term.location(0, 4):
            print("="*term.width, end="")
        with term.location(0,13):
            print("="*term.width)
            print(term.center("Move: WASD/Arrows  Place: Space/Enter  Flee: Esc/Q"))
            print("="*term.width)
        while True:

            board(pos)
            cell(x, y, term.red, term)
            key = term.inkey()

            with term.location(x, y + 1):
                print(" ", end="")

            if key.name == "KEY_ESCAPE" or key == "q":
                sys.exit()
#                                                                                   🐞 <---- This is a bug, his name is Frank
            if won==False:

                if key == "w" or key.name == "KEY_UP":
                    y = y - 2

                if key == "s" or key.name == "KEY_DOWN":
                    y = y + 2

                if key == "d" or key.name == "KEY_RIGHT":
                    x = x + 6

                if key == "a" or key.name == "KEY_LEFT":
                    x = x - 6

                if x > int(term.width / 2) + 7:
                    x = x - 6

                if x < int(term.width / 2) - 7:
                    x = x + 6

                if y > 8:
                    y = y - 2

                if y < 3:
                    y = y + 2

            if x == int((term.width / 2) - 6):
                col = 0
            if x == int((term.width / 2)):
                col = 1
            if x == int((term.width / 2) + 6):
                col = 2
            if y == 3:
                row = 0
            if y == 5:
                row = 1
            if y == 7:
                row = 2
            with term.location(0, 0):
                print(col, row)
            with term.location(0, 1):
                print(x, y)

                if key.name == "KEY_ENTER" or key == " ":
                    if following and pos[row][col] == " ":
                        pos[row][col] = "X"
                        following = not following
                        if win_check(pos, "X"):
                            with term.location(0,3):
                                print("X_won")
                            won=True
                            x_won=True
                    while not following:
                        board(pos)
                        temp = 0
                        for i in pos:
                            for a in i:
                                if a != " ":
                                    temp += 1
                        if temp != 9 and won == False:
                            with term.location(0,1):
                                print(term.center("[ALC-001]: " + random.choice(voice_line)))
                            time.sleep(1)
                            choose_from=[]
                            for i in range(0,3):
                                for a in range(0,3):
                                    if pos[i][a]==" ":
                                        choose_from.append([i, a])
                            choosen_space=random.choice(choose_from)
                            rnd_x=choosen_space[0]
                            rnd_y=choosen_space[1]
                            pos[rnd_x][rnd_y]="O"
                            following = not following
                            if win_check(pos, "O"):
                                with term.location(0,3):
                                    print("O_won")
                                won= True
                                o_won=True
                            board(pos)
                            time.sleep(0.75)
                        else:
                            break

                    
                    if temp == 9 and not won:
                        with term.location(0, 3):
                            print("draw")
                            won=True
                            return "tie"
                    if won==True:
                        if x_won:
                            pygame.mixer.music.fadeout(500)
                            transition()
                            return "x_won"
                        if o_won:
                            return "o_won"

def ActII_AI(pos):
    for i in range(3):
        if pos[i][0]==pos[i][1]!=" " and pos[i][0] != pos[i][2]!="O":
            return(i, 2)
            
        elif pos[i][0]==pos[i][2]!=" " and pos[i][0] != pos[i][1]!="O":
            return(i, 1)
            
        elif pos[i][1]==pos[i][2]!=" " and pos[i][1] != pos[i][0]!="O":
            return(i, 0)
            
        elif pos[0][i]==pos[1][i]!=" " and pos[0][i] != pos[2][i]!="O":
            return(2, i)
            
        elif pos[0][i]==pos[2][i]!=" " and pos[0][i] != pos[1][i]!="O":
            return(1, i)
            
        elif pos[1][i]==pos[2][i]!=" " and pos[1][i] != pos[0][i]!="O":
            return(0, i)
            
    if pos[0][0]==pos[1][1]!=" " and pos[0][0] != pos[2][2]!="O":
        return(2, 2)
    elif pos[0][0]==pos[2][2]!=" " and pos[0][0] != pos[1][1]!="O":
        return(1, 1)
    elif pos[2][2]==pos[1][1]!=" " and pos[1][1] != pos[0][0]!="O":
        return(0, 0)
    elif pos[0][2]==pos[1][1]!=" " and pos[0][2] != pos[2][0]!="O":
        return(2, 0)
    elif pos[0][2]==pos[2][0]!=" " and pos[0][2] != pos[1][1]!="O":
        return(1, 1)
    elif pos[2][0]==pos[1][1]!=" " and pos[2][0] != pos[0][2]!="O":
        return(0, 2)
    choose_from=[]
    for i in range(0,3):
        for a in range(0,3):
            if pos[i][a]==" ":
                choose_from.append([i, a])
    choosen_space=random.choice(choose_from)
    return choosen_space

def actIIprologe():
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with term.location(0,0):
            typewriter("At the enterance......\n")
            print("=" * 40)
            typewriter("[G4T-355]: I don't reckonise you, Trun back. Now\n")
            typewriter("[G4T-355]: I know what you want. You can't get past me.\n")
            typewriter("[G4T-355]: Many have tried. Many have failed.\n")
            pygame.mixer.music.fadeout(2)
            time.sleep(1.5)
            pygame.mixer.music.load("story_music\Future Club.mp3")
            pygame.mixer.music.play(loops=-1, start=4.0)
            transition()

def actII():
    
    x = int(term.width / 2)
    y = 3
    line_num = 0
    won=False
    following = True
    pos = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    row = 0
    col = 0
    x_won = False
    o_won = False
    tie = False

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with term.location(0, 2):
            print("="*term.width,end="")
        with term.location(0, 4):
            print("="*term.width, end="")
        with term.location(0,13):
            print("="*term.width)
            print(term.center("Move: WASD/Arrows  Place: Space/Enter  Flee: Esc/Q"))
            print("="*term.width)
        while True:

            board(pos)
            cell(x, y, term.red, term)
            key = term.inkey()

            with term.location(x, y + 1):
                print(" ", end="")

            if key.name == "KEY_ESCAPE" or key == "q":
                sys.exit()

            if won==False:
                with term.location(0,4):
                    print(following)

                if key == "w" or key.name == "KEY_UP":
                    y = y - 2

                if key == "s" or key.name == "KEY_DOWN":
                    y = y + 2

                if key == "d" or key.name == "KEY_RIGHT":
                    x = x + 6

                if key == "a" or key.name == "KEY_LEFT":
                    x = x - 6

                if x > int(term.width / 2) + 7:
                    x = x - 6

                if x < int(term.width / 2) - 7:
                    x = x + 6

                if y > 8:
                    y = y - 2

                if y < 3:
                    y = y + 2

            if x == int((term.width / 2) - 6):
                col = 0
            if x == int((term.width / 2)):
                col = 1
            if x == int((term.width / 2) + 6):
                col = 2
            if y == 3:
                row = 0
            if y == 5:
                row = 1
            if y == 7:
                row = 2
            with term.location(0, 0):
                print(col, row)
            with term.location(0, 1):
                print(x, y)
            
            if key.name == "KEY_ENTER" or key == " ":
                if following and pos[row][col] == " ":
                    pos[row][col] = "X"
                    following = not following
                    if win_check(pos, "X"):
                        with term.location(0,3):
                            print("X_won")
                        won=True
                        x_won=True
                while not following:
                    board(pos)
                    temp = 0
                    for i in pos:
                        for a in i:
                            if a != " ":
                                temp += 1
                    if temp != 9 and won == False:
                        ai_x=0
                        ai_y=0
                        choice=ActII_AI(pos)
                        ai_x=choice[0]
                        ai_y=choice[1]
                        pos[ai_x][ai_y]="O"
                        following = not following
                        if win_check(pos, "O"):
                            with term.location(0,3):
                                print("O_won")
                            won= True
                            o_won=True
                        board(pos)
                        time.sleep(0.75)
                    else:
                        break

                
                if temp == 9 and not won:
                    with term.location(0, 3):
                        print("draw")
                        won=True
                        return "tie"
                if won==True:
                    if x_won:
                        pygame.mixer.music.fadeout(500)
                        transition()
                        return "x_won"
                    if o_won:
                        return "o_won"

def story_mode():
    intro()
    actIprologe()

    while True:
        actIstate=actI()
        if actIstate=="o_won":
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                with open("ASCII/GAME_OVER.TXT", encoding="utf-8") as f:
                    line_num=0
                    for i in f:
                        with term.location(int((term.width/2)-len(i)/2), line_num+2):
                            print(i, end="")
                            line_num+=1
                        
                with term.location(0, 10):
                    typewriter("[ALC-001]: *hic* Told ya... you're no match for me, kiddo.")
                while True:
                    with term.location(0,11):
                        print(
                            f"{term.yellow}{term.center('press [ANY BUTTON] to retry')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=0.5):
                            break
                    with term.location(0,11):
                        print(
                            f"{term.black}{term.center(' ')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=1):
                            break

        if actIstate=="tie":
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                with open("ASCII/GAME_OVER.TXT", encoding="utf-8") as f:
                    line_num=0
                    for i in f:
                        with term.location(int((term.width/2)-len(i)/2), line_num+2):
                            print(i, end="")
                            line_num+=1
                        
                with term.location(0, 10):
                    typewriter("[ALC-001]: Nice try kid. But it's a tie, which means nobody won and that includes you. So what's mine stays mine.")
                while True:
                    with term.location(0,11):
                        print(
                            f"{term.yellow}{term.center('press [ANY BUTTON] to retry')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=0.5):
                            break
                    with term.location(0,11):
                        print(
                            f"{term.black}{term.center(' ')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=1):
                            break
        
        if actIstate=="x_won":
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                pygame.mixer.music.load(f"story_music/Dark Night.mp3")
                pygame.mixer.music.play(loops=-1, start=31.0)
                with term.location(0, 2):
                    typewriter("[ALC-001]: Wait... three in a row? How'd you do that? You cheated... *hic*...\n")
                    typewriter("[ALC-001]: Fine. Just take it. Take it and get out of my face.\n")
                
                while True:
                    with term.location(0, 6):
                        print(f"{term.yellow}press [ENTER] to leave{term.normal}", end="")
                        if term.inkey(timeout=0.5).name == "KEY_ENTER":
                            break
                    with term.location(0, 6):
                        print(f"{" " * 30}", end="")
                        if term.inkey(timeout=0.5).name == "KEY_ENTER":
                            break
            pygame.mixer.music.fadeout(500)
            break
        
    actIIprologe()
    actII()
    while True:
        actIstate=actII()
        if actIstate=="tie":
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                with open("ASCII/GAME_OVER.TXT", encoding="utf-8") as f:
                    line_num=0
                    for i in f:
                        with term.location(int((term.width/2)-len(i)/2), line_num+2):
                            print(i, end="")
                            line_num+=1
                        
                with term.location(0, 10):
                    typewriter("[G4T-355]: Gridlocked. Matching my defensive algorithms is mathematically notable, but equality does not grant access.")
                while True:
                    with term.location(0,11):
                        print(
                            f"{term.yellow}{term.center('press [ANY BUTTON] to retry')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=0.5):
                            break
                    with term.location(0,11):
                        print(
                            f"{term.black}{term.center(' ')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=1):
                            break
                        
        if actIstate=="o_won":
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                with open("ASCII/GAME_OVER.TXT", encoding="utf-8") as f:
                    line_num=0
                    for i in f:
                        with term.location(int((term.width/2)-len(i)/2), line_num+2):
                            print(i, end="")
                            line_num+=1
                        
                with term.location(0, 10):
                    typewriter("Place holder for G4T-355's victory line")
                while True:
                    with term.location(0,11):
                        print(
                            f"{term.yellow}{term.center('press [ANY BUTTON] to retry')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=0.5):
                            break
                    with term.location(0,11):
                        print(
                            f"{term.black}{term.center(' ')}{term.normal}",
                            end="",
                        )
                        if term.inkey(timeout=1):
                            break
        if actIstate=="o_won":
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                with term.location(0, 7):
                    print(term.center("to be continued..."))
                sys.exit()
        

    