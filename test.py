#!/usr/bin/env python3
from blessed import Terminal

term = Terminal()

with term.cbreak(), term.fullscreen(), term.mouse_enabled():
    print(term.clear)
    
    # Rajzolunk két gombot "kézzel"
    # YES gomb helye: X=10, Y=5
    # NO gomb helye:  X=20, Y=5
    print(term.move_xy(10, 5) + term.on_green("  IGEN  "))
    print(term.move_xy(20, 5) + term.on_red("  NEM   "))
    print(term.move_xy(10, 8) + "Kattints az egyikre! (vagy 'q' a kilépéshez)")

    while True:
        inp = term.inkey()

        if inp == 'q':
            break

        # Ha egérkattintás történt
        if inp.name == 'MOUSE_LEFT':
            mx, my = inp.mouse_xy
            
            # Megnézzük, hogy az IGEN gomb területén van-e az egér
            # (X 10 és 17 között, Y pedig pont az 5-ös sorban)
            if 10 <= mx <= 17 and my == 5:
                print(term.move_xy(10, 10) + term.clear_eol + "Azt mondtad: IGEN! ")
            
            # Megnézzük, hogy a NEM gomb területén van-e
            # (X 20 és 27 között, Y pedig az 5-ös sorban)
            elif 20 <= mx <= 27 and my == 5:
                print(term.move_xy(10, 10) + term.clear_eol + "Azt mondtad: NEM!  ")
            
            else:
                print(term.move_xy(10, 10) + term.clear_eol + f"Mellé ment: ({mx}, {my})")

print(term.clear)