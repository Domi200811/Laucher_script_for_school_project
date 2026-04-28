import pygame
import threading
import os


def music():
    pygame.mixer.init()
    while True:
        for music in os.listdir("soundtrack"):
            pygame.mixer.music.load(f"soundtrack/{music}")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

def text():
    print("lol")
    
t1 = threading.Thread(target=music, daemon =True)
t2 = threading.Thread(target=text,)

t1.start()
t2.start()
t1.join()
t2.join()