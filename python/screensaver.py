import curses
import time

def screensaver(screen):
    # zistim rozmery obrazovky
    height, width = screen.getmaxyx()
    y = height // 2
    x = width // 2
    dx = -1
    dy = 1
    text = 'Hello world!'

    while True:
        # update
        y = y + dy
        x = x + dx

        if y >= height:
            y = height - 1
            dy = -1

        if y <= 0:
            y = 0
            dy = 1

        if x <= 0:
            x = 0
            dx = 1

        if x >= width - len(text):
            x = width - len(text) - 1
            dx = -1

        # render
        screen.clear()
        screen.addstr(y, x, text)
        screen.refresh()
        time.sleep(0.1)

curses.wrapper(screensaver)