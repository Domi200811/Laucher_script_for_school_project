import subprocess
import sys
import os
import importlib
import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def upgrade(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])


# =================================================================
#                SZERKESZTHETŐ BEÁLLÍTÁSOK RÉSZE
# =================================================================

APP_PATH = "demo.py"  # Ide írd a fő program nevét/elérhetőségét

# =================================================================
#                SZERKESZTHETŐ RÉSZ VÉGE
# =================================================================

APP_PATH = os.path.abspath(APP_PATH)

libs = ["blessed", "pygame", "climage", "pyfiglet"]
missing_libs = []



for lib in libs:
    try:
        importlib.import_module(lib)
    except ImportError:
        missing_libs.append(lib)


if len(missing_libs) > 0:
    print("A program futtatásához az alábbi könyvtár(ak) telepítése szükséges:")
    for i in missing_libs:
        print(f"• {i}")
    while True:
        answer = input('Szeretné telepíteni őket? ["yes"/"no"] ').lower()
        if answer == "yes" or answer == "y":
            upgrade("pip")
            for i in missing_libs:
                install(i)
            break
        elif answer == "no" or answer == "n":
            print("ERROR: A program működése során hibába ütközött (itt most lenne egy fingós vicc de a szükséges könyvtár hiányában elmarad)")
            route = os.path.abspath("shitpost/reddit.html")
            print(f"SEGÍTSÉG: \x1b]8;;file://localhost/{route}\x1b\\\033[34mhttps://www.reddit.com/r/MeKnowBetter:3/comments/1szp3wb\033[0m\x1b]8;;\x1b\\")
            sys.exit()

for i in "Loading........":
    print(i, end="", flush=True)
    time.sleep(0.15)
print("")
subprocess.run([sys.executable, APP_PATH])
