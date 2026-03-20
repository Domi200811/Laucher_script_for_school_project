

import subprocess
import sys
    
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

APP_PATH="demo.py"  #Ide írd a fő program nevét/elérhetőségét

try:
    import blessed
except ImportError:
    print('A program futtatásához az alábbi könyvtár(ak) telepítése szükséges:')
    print('    • blessed')
    while True:
        Answer=input('Szeretné telepíteni őket? ["yes"/"no"] ')
        if Answer=="yes":
            install("blessed")
            subprocess.run([sys.executable, APP_PATH]) 
            break
        elif Answer=="no":
            print("A program működése hibába ütközött")
            break
else:
    print("Loading....")
    subprocess.run([sys.executable, APP_PATH])