import os
import random

random.randint(1, 500)

for i in os.listdir("shitpost/reddit-awards-main"):
    with open("demofile.txt", "a") as f:
        f.write(f'              <div class="award-item"><div class="award-number">{random.randint(1, 500)}</div> <img src="reddit-awards-main/{i}"></div>\n')