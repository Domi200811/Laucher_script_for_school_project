from blessed import Terminal
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
    term= Terminal()
    with term.hidden_cursor():
        temp=list(range(term.height))
        random.shuffle(temp)
        for i in temp:
            with term.location(0, i):
                print("█"*term.width, end="", flush=False)
                time.sleep(sleep)

def actIprologe():
    term = Terminal()
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
    tes="x"
    term = Terminal()
    line_num = 0
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
    board = f"""\
     a     b     c
  ┌─────┬─────┬─────┐
1 │  {tes}  │  {tes}  │  {tes}  │
  ├─────┼─────┼─────┤
2 │     │     │     │
  ├─────┼─────┼─────┤
3 │     │     │     │
  └─────┴─────┴─────┘
    """
    board = io.StringIO(board)
    
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        for i in board:
            with term.location(int((term.width/2)-len(i)/2), line_num+2):
                print(i, end="")
                line_num= line_num+1
        


actI()