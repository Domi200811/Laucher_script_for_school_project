import pygame
import random
import os
import time
pygame.mixer.init()
place_sound=pygame.mixer.Sound(f"sfx/boss1_sounds/{random.choice(os.listdir('sfx/boss1_sounds'))}")
place_sound.play()
time.sleep(1)