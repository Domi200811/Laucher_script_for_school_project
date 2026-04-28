from blessed import Terminal

term = Terminal()
print(term.clear + term.hide_cursor)
x=1
y=3
memory=[]

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
            print('ˇ')


            key=term.inkey()

            with term.location(y, x):
                    print(' ', end='')

            if key=="w":
                x=x-3

            if key=="s":
                x=x+3

            if key=="d":
                y=y+6
                
            if key=="a":
                y=y-6

            if key=="q":
                break

        if x>9:
            x=x-3
            
        if x<0:
            x=x+3

        if y>18:
            y=y-6
            
        if y<3:
            y=y+6

        if key==" ":
            with term.location(y, x+1):
                print("x")
                sub_memory=[y,x+1]
                memory.append(sub_memory)

print(memory)
