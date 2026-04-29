from blessed import Terminal

term = Terminal()
print(term.clear + term.hide_cursor)
x = 1
y = 3
memory_X = []
memory_O = []
following = 0
WINNING_COMBOS = [
    [[3, 2], [9, 2], [15, 2]], [[3, 5], [9, 5], [15, 5]], [[3, 8], [9, 8], [15, 8]],
    [[3, 2], [3, 5], [3, 8]], [[9, 2], [9, 5], [9, 8]], [[15, 2], [15, 5], [15, 8]],
    [[3, 2], [9, 5], [15, 8]], [[15, 2], [9, 5], [3, 8]]]
# Use the location context manager to ensure the cursor
# returns to its original position afterward

board = """\
   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     """

with term.location(0, 0):
    print(board)

with term.cbreak():
    while True:
        with term.location(y, x):
            print("ˇ")

            key = term.inkey()

            with term.location(y, x):
                print(" ", end="")

            if key == "w":
                x = x - 3

            if key == "s":
                x = x + 3

            if key == "d":
                y = y + 6

            if key == "a":
                y = y - 6

            if key == "q":
                break

        if x > 9:
            x = x - 3

        if x < 0:
            x = x + 3

        if y > 18:
            y = y - 6

        if y < 3:
            y = y + 6

        if key == " ":
            if following == 0:
                sub_memory = [y, x + 1]
                if sub_memory not in memory_X and sub_memory not in memory_O:
                    with term.location(y, x + 1):
                        print("X")
                        memory_X.append(sub_memory)
                        following = following + 1
                        if following > 1:
                            following = 0
            elif following == 1:
                sub_memory = [y, x + 1]
                if sub_memory not in memory_X and sub_memory not in memory_O:
                    with term.location(y, x + 1):
                        print("O")
                        memory_O.append(sub_memory)
                        following = following + 1
                        if following > 1:
                            following = 0
            for i in WINNING_COMBOS:
                if all(sub in memory_X for sub in i)==True:
                    with term.location(15, 3):
                            print("X wins")
                if all(sub in memory_O for sub in i)==True:
                    with term.location(15, 3):
                            print("O wins")



print(memory_X)
print(memory_O)

