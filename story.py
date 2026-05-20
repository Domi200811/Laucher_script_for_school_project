from blessed import Terminal
import time
import random
def typewriter(text, delay=0.01):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(delay)
        
def drunk_typewriter(text, delay=0.1):
    for i in text:
        print(f"{i}{" "*random.randint(0,2)}", end="", flush=True)
        time.sleep(delay)

def Drunk():
    term = Terminal()
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        
        with term.location(0, 0):
            typewriter("MEANWHILE: Somwhere at a bar....\n")
            print("="*40)
            typewriter("Do you think you can just... *hic* ...walk in here and expect me to give it to you\n")
            typewriter("I like it when it is a litle more challanging\n")
            while True:
                print(f"\r{term.yellow}press ENTER to challange him{term.normal}", end="")
                if term.inkey(timeout=0.5).name=="KEY_ENTER":
                    print("")
                    break
                print(f"\r{" "*40}", end="")
                if term.inkey(timeout=0.5).name=="KEY_ENTER":
                    print("")
                    break
            typewriter("Yeah, that's right! A duel of.... *hic* ....wits! Wait, what game are we playing again?\n")
            time.sleep(1.5)
Drunk()