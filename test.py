import math
import time
from blessed import Terminal

term = Terminal()

def spin_text(text, speed=2.0):
    angle = 0.0
    
    with term.fullscreen(), term.hidden_cursor():
        while True:
            # 1. Calculate the 'depth' and 'width' factor
            # Sine gives us the horizontal compression (-1 to 1)
            width_factor = math.sin(angle)
            # Cosine helps us simulate lighting/shading
            brightness = math.cos(angle)
            
            # 2. Determine color based on brightness
            if brightness > 0.5:
                color = term.white_bold
            elif brightness > 0:
                color = term.white
            elif brightness > -0.5:
                color = term.bright_black # Grey
            else:
                color = term.black # Darkest
            
            # 3. Calculate the scaled string
            # We "squish" the text by skipping characters or adding spacing
            # For a simple terminal effect, we'll just scale the starting position
            display_text = text
            if width_factor < 0:
                display_text = text[::-1] # Flip text when it's on the "back" side
            
            # 4. Render to screen
            # Calculate center position
            center_x = term.width // 2
            center_y = term.height // 2
            
            # Adjust X based on width_factor to keep it centered while "spinning"
            offset = int((len(text) / 2) * width_factor)
            start_x = center_x - offset
            
            print(term.home + term.clear)
            with term.location(start_x, center_y):
                # We use transform to visually squeeze the text
                # Note: True terminal scaling is limited, so we manipulate the start point
                print(color(display_text))
            
            angle += 0.1 * speed
            time.sleep(0.05)

if __name__ == "__main__":
    try:
        spin_text("3D BLESSED SPIN", speed=1.5)
    except KeyboardInterrupt:
        print(term.clear)