
import pygame
import threading
import os
from blessed import Terminal
import random
import time
import climage
import sys
from legacy.main import legacy
from story import story_mode
from pathlib import Path


term = Terminal()
music_stop = [False]
mute = [False]
kill = [False]
x_won = [0]
o_won = [0]
newgame = [True]
version = ""
mode = ""


def music(stop, kill):
    pygame.mixer.init()
    while not kill[0]:
        for music in os.listdir("soundtrack"):
            pygame.mixer.music.load(f"soundtrack/{music}")
            pygame.mixer.music.play(fade_ms=2000)

            while pygame.mixer.music.get_busy() or stop[0]:
                time.sleep(1)
                if kill[0]:
                    return


def home_screen():
    pygame.mixer.init()
    pygame.mixer.music.load(f"home_screen_tracks/lofi[3_hours].mp3")
    pygame.mixer.music.play(loops=-1, start=random.randint(0, 4800), fade_ms=1000)
    print(term.home + term.clear)
    select = pygame.mixer.Sound(f"sfx/voicebosch-menu-select-button-182476.mp3")
    highlight = pygame.mixer.Sound(f"sfx/creatorshome-on-001-337979.mp3")
    DISPLAY_TEXT_START = "[ START ]"
    DISPLAY_TEXT_LEAVE = "[ LEAVE ]"
    line_num = 0
    positon = 0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with open("ASCII/TIC-TAC-TOE.TXT", encoding="utf-8") as f:
            for i in f:
                with term.location(int(term.width / 2 - int(len(i) / 2)), line_num):
                    print(i, end="")
                    line_num += 1
        while True:

            key = term.inkey(timeout=0.1)
            if key.name == "KEY_UP":
                positon -= 1
                if positon < 0:
                    positon = 1
                highlight.play()

            if key.name == "KEY_DOWN":
                positon += 1
                if positon > 1:
                    positon = 0
                highlight.play()

            with term.location(0, line_num + 2):
                if positon == 1:
                    print(term.center(DISPLAY_TEXT_START), end="")
                if positon == 0:
                    print(
                        term.center(
                            f"{term.bold}> {DISPLAY_TEXT_START} <{term.normal}"
                        ),
                        end="",
                    )

            with term.location(0, line_num + 4):                                    #Somehow works, it shouln't but it does
                if positon == 0:
                    print(term.center(DISPLAY_TEXT_LEAVE), end="")
                if positon == 1:
                    print(
                        term.center(
                            f"{term.bold}> {DISPLAY_TEXT_LEAVE} <{term.normal}"
                        ),
                        end="",
                    )
            with term.location(0, term.height - 1):
                copyright_text = f"© 2026 DBM "
                print(
                    term.rjust(term.bright_black + copyright_text + term.normal), end=""
                )

            if key.name == "KEY_ENTER" and positon == 1:
                pygame.mixer.music.fadeout(500)
                select.play()
                time.sleep(0.5)
                sys.exit()
            if key.name == "KEY_ENTER" and positon == 0:
                select.play()
                return


def version_selector():
    pygame.mixer.init()
    print(term.home + term.clear)
    select = pygame.mixer.Sound(f"sfx/voicebosch-menu-select-button-182476.mp3")
    highlight = pygame.mixer.Sound(f"sfx/creatorshome-on-001-337979.mp3")
    DISPLAY_TEXT_LEGACY = "[ LEGACY ]"
    DISPLAY_TEXT_VISUAL = "[ VISUAL ]"
    line_num = 0
    positon = 0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with open("ASCII/SELECT_VERSION.TXT", encoding="utf-8") as f:
            for i in f:
                with term.location(int(term.width / 2 - int(len(i) / 2)), line_num):
                    print(i)
                    line_num += 1
        while True:

            key = term.inkey(timeout=0.1)
            if key.name == "KEY_UP":
                positon -= 1
                if positon < 0:
                    positon = 1
                highlight.play()

            if key.name == "KEY_DOWN":
                positon += 1
                if positon > 1:
                    positon = 0
                highlight.play()

            with term.location(0, line_num + 2):
                if positon == 1:
                    print(term.center(DISPLAY_TEXT_LEGACY), end="")
                if positon == 0:
                    print(
                        term.center(
                            f"{term.bold}> {DISPLAY_TEXT_LEGACY} <{term.normal}"
                        ),
                        end="",
                    )

            with term.location(0, line_num + 4):
                if positon == 0:
                    print(term.center(DISPLAY_TEXT_VISUAL), end="")
                if positon == 1:
                    print(
                        term.center(
                            f"{term.bold}> {DISPLAY_TEXT_VISUAL} <{term.normal}"
                        ),
                        end="",
                    )

            if key.name == "KEY_ENTER" and positon == 0:
                select.play()
                pygame.mixer.music.fadeout(300)
                return "legacy"
            if key.name == "KEY_ENTER" and positon == 1:
                select.play()
                return "visual"


def mode_selector():
    pygame.mixer.init()
    print(term.home + term.clear)
    select = pygame.mixer.Sound(
        f"sfx/freesound_community-ui_correct_button2-103167.mp3")
    select_alt=pygame.mixer.Sound(f"sfx/voicebosch-menu-select-button-182476.mp3")
    highlight = pygame.mixer.Sound(f"sfx/creatorshome-on-001-337979.mp3")
    NEW_GAME = "[ Story Mode ]"
    CONTINUE = "[ PvP ]"
    DISPLAY_TEXT_Free_Play = "[ Free Play ]"
    line_num = 0
    positon = 0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with open("ASCII/SELECT_MODE.TXT", encoding="utf-8") as f:
            for i in f:
                with term.location(int(term.width / 2 - int(len(i) / 2)), line_num):
                    print(i)
                    line_num += 1
        while True:

            key = term.inkey(timeout=0.1)
            if key.name == "KEY_UP":
                positon -= 1
                if positon < 0:
                    positon = 2
                highlight.play()

            if key.name == "KEY_DOWN":
                positon += 1
                if positon > 2:
                    positon = 0
                highlight.play()

            with term.location(0, line_num + 2):
                if positon == 0:
                    print(
                        term.center(
                            f"{term.bold}> {NEW_GAME} <{term.normal}"
                        ),
                        end="",
                    )

                else:
                    print(term.center(NEW_GAME), end="")

            with term.location(0, line_num + 4):
                if positon == 1:
                    print(
                        term.center(f"{term.bold}> {CONTINUE} <{term.normal}"),
                        end="",
                    )

                else:
                    print(term.center(CONTINUE), end="")

            with term.location(0, line_num + 6):
                if positon == 2:
                    print(
                        term.center(
                            f"{term.bold}> {DISPLAY_TEXT_Free_Play} <{term.normal}"
                        ),
                        end="",
                    )

                else:
                    print(term.center(DISPLAY_TEXT_Free_Play), end="")

            if key.name == "KEY_ENTER" and positon == 0:
                while pygame.mixer.get_busy():
                    pass
                if Path("save/save.txt").exists():
                    select_alt.play()
                else:
                    select.play()
                pygame.mixer.music.fadeout(300)
                return "story"
            if key.name == "KEY_ENTER" and positon == 1:
                while pygame.mixer.get_busy():
                    pass
                select.play()
                pygame.mixer.music.fadeout(300)
                return "PvP"
            if key.name == "KEY_ENTER" and positon == 2:
                while pygame.mixer.get_busy():
                    pass
                select.play()
                pygame.mixer.music.fadeout(300)
                return "Free_Play"

def save_selector():
    pygame.mixer.init()
    print(term.home + term.clear)
    select = pygame.mixer.Sound(
        f"sfx/freesound_community-ui_correct_button2-103167.mp3"
    )
    highlight = pygame.mixer.Sound(f"sfx/creatorshome-on-001-337979.mp3")
    NEW_GAME = "[ New Game ]"
    CONTINUE = "[ Continue ]"
    line_num = 0
    positon = 0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with open("ASCII/CONTINUE.TXT", encoding="utf-8") as f:
            for i in f:
                with term.location(int(term.width / 2 - int(len(i) / 2)), line_num):
                    print(i)
                    line_num += 1
        while True:

            key = term.inkey(timeout=0.1)
            if key.name == "KEY_UP":
                positon -= 1
                if positon < 0:
                    positon = 2
                highlight.play()

            if key.name == "KEY_DOWN":
                positon += 1
                if positon > 2:
                    positon = 0
                highlight.play()

            with term.location(0, line_num + 2):
                if positon == 0:
                    print(
                        term.center(
                            f"{term.bold}> {NEW_GAME} <{term.normal}"
                        ),
                        end="",
                    )

                else:
                    print(term.center(NEW_GAME), end="")

            with term.location(0, line_num + 4):
                if positon == 1:
                    print(
                        term.center(f"{term.bold}> {CONTINUE} <{term.normal}"),
                        end="",
                    )

                else:
                    print(term.center(CONTINUE), end="")

            with term.location(0, line_num+6):
                print(term.center("*starting a new game overwrites your previous save"))

            if key.name == "KEY_ENTER" and positon == 0:
                while pygame.mixer.get_busy():
                    pass
                select.play()
                pygame.mixer.music.fadeout(300)
                return "new"
            if key.name == "KEY_ENTER" and positon == 1:
                while pygame.mixer.get_busy():
                    pass
                select.play()
                pygame.mixer.music.fadeout(300)
                return "continue"

def game(x_won, o_won):
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
    Score_up = pygame.mixer.Sound(f"sfx/mixkit-arcade-bonus-alert-767.mp3")

    pygame.mixer.music.unpause()
    music_stop[0] = False

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

    with term.fullscreen(), term.cbreak(), term.mouse_enabled(
        report_motion=True
    ), term.hidden_cursor():

        with term.location(0, 0):
            print(term.magenta_bold + board + term.normal)

        with term.location(22, 1):
            print("WASD/Arrows: Move")

        with term.location(22, 3):
            print("Space/Enter: Place X/O")

        with term.location(22, 5):
            print("Esc/Q: Quit")

        with term.location(22, 7):
            print("N: Next Song")

            while True:
                Place = pygame.mixer.Sound(
                    f"sfx/place_sounds/{random.choice(os.listdir('sfx/place_sounds'))}"
                )

                with term.location(y, x):
                    if following == 0:
                        print(term.red_bold + "ˇ" + term.normal)
                    if following == 1:
                        print(term.blue_bold + "ˇ" + term.normal)

                    key = term.inkey()

                    with term.location(y, x):
                        print(" ", end="")

                    if key.name == "KEY_ESCAPE" or key == "q":
                        newgame[0] = False
                        return
                    if key == "n":
                        pygame.mixer.music.stop()

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
                                        with term.location(
                                            int(term.width * 0.75 - len(i) / 2),
                                            line_num2,
                                        ):
                                            print(i, end="")
                                            line_num2 = line_num2 + 1

                if game_won == True:
                    start_x = int(term.width * 0.75 - len(i) / 2)
                    if key.name and key.name.startswith("MOUSE_"):
                        if (
                            start_x <= key.mouse_xy[0] <= start_x + 18
                            and 7 <= key.mouse_xy[1] <= 11
                        ):
                            with term.location(start_x, 11):
                                print("‾" * 18, end="")
                                if key.name == "MOUSE_LEFT":
                                    break
                        else:
                            with term.location(start_x, 11):
                                print(" " * 18, end="")

                        if (
                            key.name
                            and key.name.startswith("MOUSE_")
                            and start_x + 79 <= key.mouse_xy[0] <= start_x + 92
                            and 7 <= key.mouse_xy[1] <= 11
                        ):
                            with term.location(start_x + 79, 11):
                                print("‾" * 13, end="")
                                if key.name == "MOUSE_LEFT":
                                    newgame[0] = not newgame[0]
                                    break
                        else:
                            with term.location(start_x + 79, 11):
                                print(" " * 13, end="")

    if x_won[0] > 99 or o_won[0] > 99:
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
            if current_winner.lower() == "x":
                with open(f"numbers/{x_won[0]-1}.txt", encoding="utf-8") as f:
                    for i, z in zip(f, range(7)):
                        with term.location(int((term.width / 4) + 7), 2 + z):
                            print(i, end="")
            else:
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
            if current_winner.lower() == "o":
                with open(f"numbers/{o_won[0]-1}.txt", encoding="utf-8") as f:
                    for i, z in zip(f, range(7)):
                        with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                            print(i, end="")
            else:
                with open(f"numbers/{o_won[0]}.txt", encoding="utf-8") as f:
                    for i, z in zip(f, range(7)):
                        with term.location((int((term.width / 4) * 3) + 7), 2 + z):
                            print(i, end="")
            time.sleep(2)
        print(
            climage.convert("ASCII/TOUCH_GRASS.png", width=200, is_unicode=True), end=""
        )
        return

    if current_winner == "X":
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
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
            time.sleep(2)

    if current_winner == "O":
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
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
            time.sleep(2)

    if current_winner == "":
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
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
            time.sleep(2)

    counter = 0
    if newgame[0] == False:
        if x_won[0] > o_won[0]:
            with open("ASCII/PLAYER_1_WON.TXT", encoding="utf-8") as f:
                for i in f:
                    with term.location(int(term.width / 2 - (len(i) / 2)), counter):
                        print(i)
                        counter = counter + 1

        if x_won[0] < o_won[0]:
            with open("ASCII/PLAYER_2_WON.TXT", encoding="utf-8") as f:
                for i in f:
                    with term.location(int(term.width / 2 - (len(i) / 2)), counter):
                        print(i)
                        counter = counter + 1

        if x_won[0] == o_won[0]:
            with open("ASCII/ITS_A_TIE.TXT", encoding="utf-8") as f:
                for i in f:
                    with term.location(int(term.width / 2 - (len(i) / 2)), counter):
                        print(i)
                        counter = counter + 1


home_screen()
version = version_selector()
if version == "visual":
    mode = mode_selector()

if mode == "story":
    if Path("save/save.txt").exists():
        save_choice=save_selector()
        if save_choice=="new":
            story_mode()
        if save_choice=="continue":
            with open("save/save.txt", encoding="utf-8") as f:
                progress=f.readlines()
            story_mode(int(progress[0]))
    else:
        story_mode()
if mode == "PvP":
    t1 = threading.Thread(
        target=music,
        daemon=True,
        args=(
            music_stop,
            kill,
        ),
    )
    t1.start()
    while newgame[0] and x_won[0] < 100 and o_won[0] < 100:
        game(x_won, o_won)

if mode == "Free_Play":
    print("lol")

elif version == "legacy":
    legacy()
