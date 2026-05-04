import pygame
import threading
import os
from blessed import Terminal
import random
import time


music_stop = [False]
mute = [False]
kill = [False]
x_won = [0]
o_won = [0]
newgame=[True]

def music(stop, kill):
    pygame.mixer.init()
    while not kill[0]:
        for music in os.listdir("soundtrack"):
            pygame.mixer.music.load(f"soundtrack/{music}")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() or stop[0]:
                time.sleep(1)
                if kill[0]:
                    return


def game(x_won, o_won):
    term = Terminal()
    print(term.clear + term.hide_cursor)
    x = 1
    y = 3
    memory_X = []
    memory_O = []
    current_winner = ""
    following = 0
    WINNING_COMBOS = [
        [[3, 2], [9, 2], [15, 2]],
        [[3, 5], [9, 5], [15, 5]],
        [[3, 8], [9, 8], [15, 8]],
        [[3, 2], [3, 5], [3, 8]],
        [[9, 2], [9, 5], [9, 8]],
        [[15, 2], [15, 5], [15, 8]],
        [[3, 2], [9, 5], [15, 8]],
        [[15, 2], [9, 5], [3, 8]],
    ]

    Place = pygame.mixer.Sound(
        f"sfx/place_sounds/{random.choice(os.listdir('sfx/place_sounds'))}"
    )
    P_slam = pygame.mixer.Sound(f"sfx/P_slam.mp3")
    Win_slam = pygame.mixer.Sound(f"sfx/Win_slam.mp3")
    Score_up= pygame.mixer.Sound(f"sfx/mixkit-arcade-bonus-alert-767.mp3")

    pygame.mixer.music.unpause()
    music_stop[0]=False

    game_won = False
    line_num = 0
    line_num2 = 0

    board = """\
   a     b     c
      |     |     
1     |     |     
 _____|_____|_____
      |     |     
2     |     |     
 _____|_____|_____
      |     |     
3     |     |     
      |     |     """


    with term.fullscreen(), term.cbreak(), term.mouse_enabled(report_motion=True):

        with term.location(0, 0):
            print(term.magenta_bold + board + term.normal)

        with term.location(22, 1):
            print("WASD/Arrows: Move")

        with term.location(22, 3):
            print("Space/Enter: Place X/O")

        with term.location(22, 5):
            print("Esc/Q: Quit")
        
        with term.location(22, 7):
            print(term.height)

            while True:
                with term.location(y, x):
                    if following == 0:
                        print(term.red_bold + "ˇ" + term.normal)
                    if following == 1:
                        print(term.blue_bold + "ˇ" + term.normal)

                    key = term.inkey()

                    with term.location(y, x):
                        print(" ", end="")

                    if key.name == "KEY_ESCAPE" or key == "q":
                        newgame[0]=False
                        return

                    if game_won == False:
                        if key == "w" or key.name == "KEY_UP":
                            x = x - 3

                        if key == "s" or key.name == "KEY_DOWN":
                            x = x + 3

                        if key == "d" or key.name == "KEY_RIGHT":
                            y = y + 6

                        if key == "a" or key.name == "KEY_LEFT":
                            y = y - 6

                    if x > 9:
                        x = x - 3

                    if x < 0:
                        x = x + 3

                    if y > 18:
                        y = y - 6

                    if y < 3:
                        y = y + 6

                    if key == " " or key.name == "KEY_ENTER":
                        if following == 0:
                            sub_memory = [y, x + 1]
                            if (
                                sub_memory not in memory_X
                                and sub_memory not in memory_O
                            ):
                                with term.location(y, x + 1):
                                    Place.play()
                                    print(term.white_bold + "X" + term.normal)
                                    time.sleep(0.05)
                                with term.location(y, x + 1):
                                    print(term.yellow_bold + "X" + term.normal)
                                    time.sleep(0.05)
                                with term.location(y, x + 1):
                                    print(term.red_bold + "X" + term.normal)
                                    memory_X.append(sub_memory)
                                    following = following + 1
                                    if following > 1:
                                        following = 0
                        elif following == 1:
                            sub_memory = [y, x + 1]
                            if (
                                sub_memory not in memory_X
                                and sub_memory not in memory_O
                            ):
                                with term.location(y, x + 1):
                                    Place.play()
                                    print(term.white_bold + "O" + term.normal)
                                    time.sleep(0.05)
                                with term.location(y, x + 1):
                                    print(term.yellow_bold + "O" + term.normal)
                                    time.sleep(0.05)
                                with term.location(y, x + 1):
                                    print(term.blue_bold + "O" + term.normal)
                                    memory_O.append(sub_memory)
                                    following = following + 1
                                    if following > 1:
                                        following = 0
                        for i in WINNING_COMBOS:
                            if all(sub in memory_X for sub in i) == True:
                                game_won = True
                                x_won[0] = x_won[0] + 1
                                current_winner = "X"
                                with open("ASCII/P1.txt", encoding="utf-8") as f:
                                    for i in f:
                                        if line_num == 0:
                                            pygame.mixer.music.pause()
                                            music_stop[0] = not music_stop[0]
                                            P_slam.play()
                                        with term.location(50, line_num):
                                            print(i, end="")
                                            line_num = line_num + 1
                                            if line_num == 7:
                                                time.sleep(2)
                                                Win_slam.play()
                                    time.sleep(3)
                                    pygame.mixer.music.unpause()
                                    music_stop[0] = not music_stop[0]
                            if all(sub in memory_O for sub in i) == True:
                                game_won = True
                                o_won[0] = o_won[0] + 1
                                current_winner = "O"
                                with open("ASCII/P2.txt", encoding="utf-8") as f:
                                    for i in f:
                                        if line_num == 0:
                                            pygame.mixer.music.pause()
                                            music_stop[0] = not music_stop[0]
                                            P_slam.play()
                                        with term.location(50, line_num):
                                            print(i, end="")
                                            line_num = line_num + 1
                                            if line_num == 7:
                                                time.sleep(2)
                                                Win_slam.play()
                                    time.sleep(3)
                                    pygame.mixer.music.unpause()
                                    music_stop[0] = not music_stop[0]
                        if len(memory_O) + len(memory_X) == 9 and line_num == 0:
                            game_won = True
                            with open("ASCII/TIE.txt", encoding="utf-8") as f:
                                pygame.mixer.music.pause()
                                music_stop[0] = not music_stop[0]
                                time.sleep(1)
                                Win_slam.play()
                                for i in f:
                                    with term.location(50, line_num):
                                        print(i, end="")
                                        line_num = line_num + 1
                            time.sleep(3)
                            pygame.mixer.music.unpause()
                            music_stop[0] = not music_stop[0]

                        if game_won == True:
                            with open("ASCII/REMATCH.txt", encoding="utf-8") as f:
                                for i in f:
                                    with term.location(90, line_num2):
                                        print(i, end="")
                                        line_num2 = line_num2 + 1
                if game_won == True:
                    if (
                        key.name
                        and key.name.startswith("MOUSE_")
                        and 90 <= key.mouse_xy[0] <= 108
                        and 7 <= key.mouse_xy[1] <= 11
                    ):
                        with term.location(90, 11):
                            print("‾" * 18, end="")
                            if key.name == "MOUSE_LEFT":
                                break
                    else:
                        with term.location(90, 11):
                            print(" " * 18, end="")

                    if (
                        key.name
                        and key.name.startswith("MOUSE_")
                        and 169 <= key.mouse_xy[0] <= 182
                        and 7 <= key.mouse_xy[1] <= 11
                    ):
                        with term.location(169, 11):
                            print("‾" * 13, end="")
                            if key.name == "MOUSE_LEFT":
                                newgame[0]= not newgame[0]
                                break
                    else:
                        with term.location(169, 11):
                            print(" " * 13, end="")

    if current_winner == "X":
        with term.fullscreen(), term.cbreak():
            pygame.mixer.music.pause()
            music_stop[0] = not music_stop[0]
            with open("ASCII/P1.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4)) - 19), 2 + z):
                        print(i, end="")
            with open("ASCII/DOUBLEPOINT.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4)) + 2), 2 + z):
                        print(i, end="")
            with open(f"numbers/{x_won[0]-1}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location(int((term.width / 4) + 7), 2 + z):
                        print(i, end="")
            with open("ASCII/P2.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) - 21), 2 + z):
                        print(i, end="")
            with open("ASCII/DOUBLEPOINT.TXT", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 2), 2 + z):
                        print(i, end="")
            with open(f"numbers/{o_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                        print(i, end="")
            time.sleep(1)
            Score_up.play()
            with open(f"numbers/{x_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location(int((term.width / 4) + 7), 2 + z):
                        print(" " * 30, end="")
            with open(f"numbers/{x_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location(int((term.width / 4) + 7), 2 + z):
                        print(term.gold + i + term.normal, end="")
            time.sleep(1)

    if current_winner == "O":
        with term.fullscreen(), term.cbreak():
            pygame.mixer.music.pause()
            music_stop[0] = not music_stop[0]
            with open("ASCII/P1.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4)) - 19), 2 + z):
                        print(i, end="")
            with open("ASCII/DOUBLEPOINT.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4)) + 2), 2 + z):
                        print(i, end="")
            with open(f"numbers/{x_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location(int((term.width / 4) + 7), 2 + z):
                        print(i, end="")
            with open("ASCII/P2.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) - 21), 2 + z):
                        print(i, end="")
            with open("ASCII/DOUBLEPOINT.TXT", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 2), 2 + z):
                        print(i, end="")
            with open(f"numbers/{o_won[0]-1}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                        print(i, end="")
            time.sleep(1)
            Score_up.play()
            with open(f"numbers/{o_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                        print(" " * 30, end="")
            with open(f"numbers/{o_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                        print(term.gold + i + term.normal, end="")
            time.sleep(1)

    if current_winner == "":
        with term.fullscreen(), term.cbreak():
            pygame.mixer.music.pause()
            music_stop[0] = not music_stop[0]
            with open("ASCII/P1.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4)) - 19), 2 + z):
                        print(i, end="")
            with open("ASCII/DOUBLEPOINT.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4)) + 2), 2 + z):
                        print(i, end="")
            with open(f"numbers/{x_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location(int((term.width / 4) + 7), 2 + z):
                        print(i, end="")
            with open("ASCII/P2.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) - 21), 2 + z):
                        print(i, end="")
            with open("ASCII/DOUBLEPOINT.TXT", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 2), 2 + z):
                        print(i, end="")
            with open(f"numbers/{o_won[0]}.txt", encoding="utf-8") as f:
                for i, z in zip(f, range(7)):
                    with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                        print(i, end="")
            time.sleep(1)
    
    counter=0
    if newgame[0]==False:
        if x_won[0]>o_won[0]:
            with open("ASCII/PLAYER_1_WON.TXT", encoding="utf-8") as f:
                for i in f:
                    with term.location(int(term.width/2-(len(i)/2)), counter):
                        print(i)
                        counter= counter+1
    
        if x_won[0]<o_won[0]:
            with open("ASCII/PLAYER_2_WON.TXT", encoding="utf-8") as f:
                for i in f:
                    with term.location(int(term.width/2-(len(i)/2)), counter):
                        print(i)
                        counter= counter+1
        
        if x_won[0]==o_won[0]:
            with open("ASCII/ITS_A_TIE.TXT", encoding="utf-8") as f:
                for i in f:
                    with term.location(int(term.width/2-(len(i)/2)), counter):
                        print(i)
                        counter= counter+1




t1 = threading.Thread(
    target=music,
    daemon=True,
    args=(
        music_stop,
        kill,
    ),
)
t1.start()
while newgame[0]:

    t2 = threading.Thread(
        target=game,
        args=(
            x_won, 
            o_won,
        )
    )



    t2.start()
    t2.join()