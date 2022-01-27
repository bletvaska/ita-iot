import curses
import time
import random

KEY_ESC = 27

def snake(screen):
    # init curses

    # nacitavanie klaves cez getch() bude neblokujuci
    screen.nodelay(True)
    # skryt kurzor
    curses.curs_set(0)

    key = None
    rows, cols = screen.getmaxyx()
    snake = [
        (8, 10),  # head
        (9, 10),
        (10, 10),
    ]
    foods = []
    for _ in range(20):
        #! FIXME osetrite, aby sa to jedlo nevygenerovalo tam, kde je hadik
        food = (random.randint(1, rows - 2),
            random.randint(1, cols - 2))
        foods.append(food)

    # pozicia a smer hadika na zaciatku
    y = snake[0][0]
    x = snake[0][1]
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
            screen.addstr(rows//2, cols//2, 'Hlavou múr neprerazíš.')
            screen.refresh()
            time.sleep(2)
            break

        # update hadik
        # head
        snake.insert(0, (y, x))
        # tail
        snake.pop()

        # render
        screen.clear()
        screen.addstr(0, 0, f'Snake Game {key}')

        # render hadik
        for part in snake:
            screen.addstr(part[0], part[1], 'o')

        screen.refresh()
        time.sleep(0.5)

curses.wrapper(snake)