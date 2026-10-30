# TIC TAC TOE

## Játék menete

### Játékmód kiválasztása

- Függőségek letöltése
- Start-tal elkezdeni a játékot
- Játékmód kiválasztása
    - Legacy
    - Visual 

### Maga a játék

- Nyilakkal mozgatjuk a kurzort
- Kiválasztjuk, hogy hova szeretnénk tenni az X-et vagy a O-t
- Következő játékos következik

### Visszavágó vagy kilépés

- Wins felirat megjelenése
- Score board
- Rematch
    - Igen
    - Nem

## Dominik

- A kód egésze szinte
.Kód végső összeillesztése
- 80 órát fektetett bele

### Dominik code snippetje
```
def music(stop, kill):
    pygame.mixer.init()
    while not kill[0]:
        for music in os.listdir("soundtrack"):
            pygame.mixer.music.load(f"soundtrack/{music}")
            pygame.mixer.music.play(fade_ms=2000)

            while pygame.mixer.music.get_busy() or stop[0]:
                time.sleep(1)
                if kill[0]:
                    return
```
## Bálint

- A kód legacy része

### Bálint code snippete
```
    def check_draw(board):
            szamlalo = 0
            for i in board[:1]:
                for a in i[:1]:
                    if a != None:
                        szamlalo += 1
            if szamlalo == 9:
                return True
            else: return False
```

## Marci
- PPT
- README
- Segítség a legacy-ban (amikor tudtam)
### Marci code snippetje
```
    """     def check_draw(board):
        global dontetlen_x_szamlalo
        dontetlen_x_szamlalo = 0
        for i in board:
            for a in i:
                if a == "X":
                    dontetlen_x_szamlalo +=1
        if dontetlen_x_szamlalo == 5 and not check_winnerX :
            return True """
```

## SWOT
### Erőségek:  
- Zene 
- vizuális 

### Gyengeségek:
- Nehezen bővíthető
### Lehetőségek:
- Story mód bővítése
### Veszélyek:
- A függőségek letöltése elijesztheti a játékosokat
