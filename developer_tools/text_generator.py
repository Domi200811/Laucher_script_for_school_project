from pyfiglet import Figlet
def font_generator(text, format):
    f = Figlet(font=format)
    print(f.renderText(text))