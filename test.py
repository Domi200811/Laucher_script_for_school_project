from blessed import Terminal
import time
term=Terminal()
with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    with open("ASCII/CREDITS.TXT", encoding="UTF-8") as f:
        with term.location(0,term.height):
            for i in f:
                print(term.center(i))
                time.sleep(0.75)
    time.sleep(3)