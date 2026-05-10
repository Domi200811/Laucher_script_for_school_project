import sys
from blessed import Terminal

term = Terminal()

def home_screen():
    print(term.home + term.clear)
    DISPLAY_TEXT_START="[ START ]"
    DISPLAY_TEXT_LEAVE="[ LEAVE ]"
    line_num=0
    positon=0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with open("ASCII/TIC-TAC-TOE.TXT", encoding="utf-8") as f:
            for i in f:
                with term.location(int(term.width/2-int(len(i)/2)), line_num):
                    print(i)
                    line_num+=1
        while True:
            
            key=term.inkey(timeout=0.1)
            if key.name=="KEY_UP":
                positon-=1
                if positon<0:
                    positon=1
            
            if key.name=="KEY_DOWN":
                positon+=1
                if positon>1:
                    positon=0
            
            
                
            with term.location(0, term.height-4):
                if positon == 1:
                    print(term.center(" "), end="") 
                    print(term.center(DISPLAY_TEXT_START), end="")
                if positon == 0:
                    print(term.center(" "), end="")
                    print(term.center(f"{term.bold}> {DISPLAY_TEXT_START} <{term.normal}"), end="")
            
            with term.location(0, term.height-2):
                if positon == 0:
                    print(term.center(" "), end="") 
                    print(term.center(DISPLAY_TEXT_LEAVE), end="")
                if positon == 1:
                    print(term.center(" "), end="")
                    print(term.center(f"{term.bold}> {DISPLAY_TEXT_LEAVE} <{term.normal}"), end="")
            
            if key.name=="KEY_ENTER" and positon == 1:
                sys.exit()
                break
            if key.name=="KEY_ENTER" and positon == 0:
                version_selector()
                break

def version_selector():
    print(term.home + term.clear)
    DISPLAY_TEXT_LEGACY= "[ LEGACY ]"
    DISPLAY_TEXT_GRAPHICAL= "[ VISUAL ]"
    line_num=0
    positon=0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        with open("ASCII/SELECT_VERSION.TXT", encoding="utf-8") as f:
            for i in f:
                with term.location(int(term.width/2-int(len(i)/2)), line_num):
                    print(i)
                    line_num+=1
        while True:
            
            key=term.inkey(timeout=0.1)
            if key.name=="KEY_UP":
                positon-=1
                if positon<0:
                    positon=1
            
            if key.name=="KEY_DOWN":
                positon+=1
                if positon>1:
                    positon=0
            
            
                
            with term.location(0, term.height-4):
                if positon == 1:
                    print(term.center(DISPLAY_TEXT_LEGACY), end="")
                if positon == 0:
                    print(term.center(f"{term.bold}> {DISPLAY_TEXT_LEGACY} <{term.normal}"), end="")
            
            with term.location(0, term.height-2):
                if positon == 0:
                    print(term.center(DISPLAY_TEXT_GRAPHICAL), end="")
                if positon == 1:
                    print(term.center(f"{term.bold}> {DISPLAY_TEXT_GRAPHICAL} <{term.normal}"), end="")
            
            if key.name=="KEY_ENTER" and positon == 1:
                break
            if key.name=="KEY_ENTER" and positon == 0:
                break


home_screen()