import time
import pygame
import random
import os
pygame.mixer.init()

Place_value = (f"sfx/place_sounds/{random.choice(os.listdir('sfx/place_sounds'))}")
Place= pygame.mixer.Sound(Place_value)




while True:
    Place_value = (f"sfx/place_sounds/{random.choice(os.listdir('sfx/place_sounds'))}")
    Place= pygame.mixer.Sound(Place_value)
    print(Place_value)
    Place.play()
    time.sleep(1)