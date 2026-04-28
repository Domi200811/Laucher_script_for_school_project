import pygame
import threading


def music():
    pygame.mixer.init()
    pygame.mixer.music.load("Action 52 - CheetahMen Theme.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def text():
    print("lol")
    
t1 = threading.Thread(target=music, daemon =True)
t2 = threading.Thread(target=text, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()