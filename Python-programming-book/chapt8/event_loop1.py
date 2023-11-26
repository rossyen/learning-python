# event_loop1.py
from graphics import *

def main():
    win = GraphWin("Color Window", 500, 500)

    # Event loop: handle key presses until user presses the "q" key.
    while True:
        key = win.getKey()
        if key == "q": # loop exit
            break

        # process the key
        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgrey")
        elif key == "b":
            win.setBackground("lightblue")

    # exit program
    win.close()

main()