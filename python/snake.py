#!/usr/bin/env python3

import curses
import time
import random

STATE_PLAYING = 0
STATE_QUIT = 1
STATE_ATE_HIMSELF = 2
STATE_ATE_POISON = 3
STATE_HIT_BORDER = 4

KEY_ESC = 27


def print_center(screen, text: str):
    rows, cols = screen.getmaxyx()
    y = rows // 2
    x = cols // 2 - len(text) // 2
    screen.addstr(y, x, text)


def generate_item(screen, items):
    rows, cols = screen.getmaxyx()
    item = None

    # generate item till it's outside of list of items
    while item is None or item in items:
        item = (random.randint(1, rows - 2),
                random.randint(1, cols - 2))
    
    return item


def snake(screen):
    # init curses
    # nacitavanie klaves cez getch() bude neblokujuci
    screen.nodelay(True)
    # skryt kurzor
    curses.curs_set(0)

    rows, cols = screen.getmaxyx()

    # hadik
    snake = [
        (8, 10),  # head
        (9, 10),
        (10, 10),
    ]
    head = snake[0]

    # generovanie jedla
    foods = []
    for _ in range(30):
        food = generate_item(screen, snake)
        foods.append(food)

    # generovanie otravy
    poison = []
    for _ in range(30):
        item = generate_item(screen, snake + foods)
        poison.append(item)

    # pozicia a smer hadika na zaciatku
    dx = 0
    dy = -1
    speed = 0.5

    state = STATE_PLAYING

    # herna slucka
    while state == STATE_PLAYING:
        # update
        head = snake[0]

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
            elif key == KEY_ESC:
                state = STATE_QUIT
                break

        # aktualizujem polohu hadika
        head = ( head[0] + dy, head[1] + dx )

        # trafil som kapustu?
        if head in foods:
            foods.remove(head)
            food = generate_item(screen, snake + poison)
            foods.append(food)
            speed = speed - 0.01
        else:
            # ak som netrafil kapustu, tak odstranim chvost (hybem sa)
            snake.pop()

        # trafil som otravu?
        if head in poison:
            state = STATE_ATE_POISON
            break

        # trafil hadik o stenu?
        if head[0] in (0, rows - 1) or head[1] in (0, cols - 1):
            state = STATE_HIT_BORDER
            break

        # zozral hadik sam seba?
        if head in snake[1:]:
            state = STATE_ATE_HIMSELF
            break

        # posun novu polohu hlavicky na zaciatok zoznamu
        snake.insert(0, head)

        # render
        screen.clear()
        # nakresli okraj/ramik
        screen.border('|', '|', '-', '-', '+', '+', '+', '+')
        screen.addstr(0, 3, f' Dĺžka: {len(snake)}  Rýchlosť: {speed:.2} ')

        # render food
        for food in foods:
            screen.addstr(food[0], food[1], '♠')

        # render poison
        for item in poison:
            screen.addstr(item[0], item[1], '☠')

        # render hadik
        screen.addstr(head[0], head[1], '⚉')
        for part in snake[1:]:
            screen.addstr(part[0], part[1], '⬤')

        screen.refresh()
        time.sleep(speed)

    # zobrazenie zaverecnej spravy podla stavu
    if state == STATE_ATE_POISON:
        print_center(screen, 'Bleah. Ta toto nebola kapusta :-(')
    elif state == STATE_HIT_BORDER:
        print_center(screen, 'Hlavou múr neprerazíš.')
    elif state == STATE_ATE_HIMSELF:
        print_center(screen, 'Sám seba nežerem.')

    screen.refresh()
    time.sleep(2)

curses.wrapper(snake)

