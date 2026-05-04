from blessed import Terminal

term=Terminal

with term.fullscreen(), term.cbreak():
    with open("ASCII/P1.txt", encoding="utf-8") as f:
        for i, z in zip(f, range(7)):
            with term.location((int((term.width / 4))-19), 2+z):
                print(i, end="")
    with open(f"numbers/{x_won}.txt", encoding="utf-8") as f:
        for i, z in zip(f, range(7)):
            with term.location(int((term.width / 4)), 2+z):
                print(i, end="")
    term.inkey()