from blessed import Terminal
import time
import random

def transition():
    term= Terminal()
    with term.hidden_cursor():
        temp=list(range(term.height))
        random.shuffle(temp)
        for i in temp:
            with term.location(0, i):
                print("█"*term.width, end="", flush=False)
                time.sleep(0.1)
        term.inkey()

transition()