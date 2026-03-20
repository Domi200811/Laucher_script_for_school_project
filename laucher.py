import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# =================================================================
#                SZERKESZTHETŐ BEÁLLÍTÁSOK RÉSZE
# =================================================================

APP_PATH = "demo.py"     # Ide írd a fő program nevét/elérhetőségét

# =================================================================
#                SZERKESZTHETŐ RÉSZ VÉGE
# ================================================================= 

try:
    import blessed
except ImportError:
    print("A program futtatásához az alábbi könyvtár(ak) telepítése szükséges:")
    print("    • blessed")
    while True:
        answer = input('Szeretné telepíteni őket? ["yes"/"no"] ').lower()
        if answer == "yes":
                install("blessed")
                subprocess.run([sys.executable, APP_PATH])
                sys.exit()
        elif answer == "no":
            print("A program működése hibába ütközött")
            sys.exit()
else:
    print("Loading....")
    subprocess.run([sys.executable, APP_PATH])

