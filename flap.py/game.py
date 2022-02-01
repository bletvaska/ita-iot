WIDTH = 288
HEIGHT = 512
TITLE = 'Namakaná bavka'
GRAVITY = 0.3

flappy = Actor('flappy')
flappy.x = WIDTH / 2
flappy.y = HEIGHT / 2
flappy.ay = 0

def update():
    flappy.ay = flappy.ay + GRAVITY
    flappy.y = flappy.y + flappy.ay

def draw():
    screen.clear()
    flappy.draw()