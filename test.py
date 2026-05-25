import time
from blessed import Terminal

def intro():
    term = Terminal()
    line_num=0
    # 1. Define the grayscale color codes for 256-color terminals.
    # In the 256-color palette, codes 232 to 255 are a clean gradient from dark gray to near-white.
    # We include '15' at the end for pure brilliant white.
    grayscale_palette = [16, 16, 16] + list(range(232, 256)) + [15]
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.clear)
        time.sleep(3)
        logo=None
        # 2. Loop through the colors to create the brightening effect
        with open("ASCII/LOGO.TXT", encoding="utf-8") as f:
            logo=f.readlines()
        for color_code in grayscale_palette:
        # Move cursor to home (0,0) so we overwrite the same line safely
        
            for i in logo:
                with term.location(int((term.width/2)-len(i)/2), line_num):
                    print(term.color(color_code) + i + term.normal, end='', flush=True)
                    line_num+=1
            line_num=0
        # Adjust this sleep timer to make the fade faster or slower
            time.sleep(0.06)
            
        term.inkey()

if __name__ == "__main__":
    fade_in_text()