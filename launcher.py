import subprocess
import sys
import os
import importlib
import time


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# =================================================================
#                SZERKESZTHETŐ BEÁLLÍTÁSOK RÉSZE
# =================================================================

APP_PATH = "demo.py"  # Ide írd a fő program nevét/elérhetőségét

# =================================================================
#                SZERKESZTHETŐ RÉSZ VÉGE
# =================================================================

APP_PATH = os.path.abspath(APP_PATH)

libs = ["blessed", "pygame"]
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
            for i in missing_libs:
                install(i)
            break
        elif answer == "no" or answer == "n":
            print("A program működése során hibába ütközött")
            sys.exit()

print("Loading....")
time.sleep(1)
subprocess.run([sys.executable, APP_PATH])
