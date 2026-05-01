import pygame
import threading
import os
from blessed import Terminal
import random
import time

music_stop = [False]
mute = [False]


def music(stop, mute):
    pygame.mixer.init()
    while True:
        for music in os.listdir("soundtrack"):
            pygame.mixer.music.load(f"soundtrack/{music}")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() or stop[0] or mute[0]:
                time.sleep(1)


def game():
    term = Terminal()
    print(term.clear + term.hide_cursor)
    x = 1
    y = 3
    memory_X = []
    memory_O = []
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

    with term.location(0, 0):
        print(term.magenta_bold + board + term.normal)

    with term.location(22, 1):
        print("WASD/Arrows: Move")

    with term.location(22, 3):
        print("Space/Enter: Place X/O")

    with term.location(22, 5):
        print("Esc/Q: Quit")

    with term.cbreak():
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
                    break

                if key == "m":
                    mute[0] = not mute[0]

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
                        if sub_memory not in memory_X and sub_memory not in memory_O:
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
                        if sub_memory not in memory_X and sub_memory not in memory_O:
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


t1 = threading.Thread(target=music, daemon=True, args=(music_stop, mute,))
t2 = threading.Thread(
    target=game,
)

t1.start()
t2.start()
t2.join()
