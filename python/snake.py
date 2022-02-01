import curses
import time
import random

# domaca
#
# 1. nakreslite ramik okolo obrazovky
# 2. hlavicku nakreslite ako znak 'v' a zvysok tela bude pekne 'o'
# 3. refaktorujte, co mozete a viete
#    * uz teraz mame opakujuce sa casti kodu -> funkcia
# 4. osetrite, aby sa to jedlo nevygenerovalo tam, kde je hadik
# 5. rozsypte po hernom plane otravu
#    * ked wurmi zozerie otravu, zomrie
#    * otrava sa negeneruje cez kapustu a ani cez hadika ani pred hadikom


def print_center(screen, text:str):
    rows, cols = screen.getmaxyx()
    y = rows // 2
    x = cols // 2 - len(text) // 2
    screen.addstr(y, x, text)


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

        # trafil som kapustu?
        eating = False
        if (y, x) in foods:
            eating = True
            foods.remove((y,x))
            food = (random.randint(1, rows - 2),
                    random.randint(1, cols - 2))
            foods.append(food)

        # trafil hadik o stenu?
        if y == 0 or y == rows - 1 or x == 0 or x == cols - 1:
            print_center(screen, 'Hlavou múr neprerazíš.')
            #screen.addstr(rows//2, cols//2, 'Hlavou múr neprerazíš.')
            screen.refresh()
            time.sleep(2)
            break

        # zozral hadik sam seba?
        if (y, x) in snake[1:]:
            print_center(screen, 'Sám seba nežerem.')
            #screen.addstr(rows//2, cols//2, 'Sám seba nežerem.')
            screen.refresh()
            time.sleep(2)
            break

        # update hadik
        # head
        snake.insert(0, (y, x))
        # tail
        if not eating:
            snake.pop()

        # render
        screen.clear()
        # nakresli okraj/ramik
        screen.border('|', '|', '-', '-', '+', '+', '+', '+')

        screen.addstr(0, 3, f' Dĺžka: {len(snake)} ')

        # render food
        for food in foods:
            screen.addstr(food[0], food[1], '*')

        # render hadik
        for part in snake:
            screen.addstr(part[0], part[1], 'o')

        screen.refresh()
        time.sleep(0.5)

curses.wrapper(snake)