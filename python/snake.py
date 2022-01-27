import curses
import time

KEY_ESC = 27

def snake(screen):
    # init curses

    # nacitavanie klaves cez getch() bude neblokujuci
    screen.nodelay(True)
    # skryt kurzor
    curses.curs_set(0)

    key = None
    rows, cols = screen.getmaxyx()

    # pozicia a smer hadika na zaciatku
    y = 10
    x = 10
    dx = 0
    dy = -1

    while key != KEY_ESC:
        # update
        # zistujem, aky klaves bol stlaceny
        key = screen.getch()

        if key != -1:
            if key == curses.KEY_RIGHT:
                dx = 1
                dy = 0
            elif key == curses.KEY_LEFT:
                dx = -1
                dy = 0
            elif key == curses.KEY_UP:
                dx = 0
                dy = -1
            elif key == curses.KEY_DOWN:
                dx = 0
                dy = 1

        # aktualizujem polohu hadika
        y = y + dy
        x = x + dx

        # trafil hadik o stenu?
        if y == 0 or y == rows - 1 or x == 0 or x == cols - 1:
            screen.addstr(rows//2, cols//2, 'Hlavou mur neprerazis.')
            screen.refresh()
            time.sleep(2)
            break


        # render
        screen.clear()
        screen.addstr(0, 0, f'Snake Game {key}')

        screen.addstr(y, x, 'o')
        screen.refresh()
        time.sleep(0.5)

curses.wrapper(snake)