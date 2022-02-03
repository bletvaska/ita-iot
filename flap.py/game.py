WIDTH = 288
HEIGHT = 512
TITLE = 'Flap.py'
GRAVITY = 0.3

flappy = Actor('flappy')
flappy.x = WIDTH / 2
flappy.y = HEIGHT / 2
flappy.ay = 0
flappy.score = 0

upper_pipe = Actor('pipe.upper')
upper_pipe.left = WIDTH

def update():
    # update flappy
    flappy.ay = flappy.ay + GRAVITY
    flappy.y = flappy.y + flappy.ay

    # update pipes
    upper_pipe.x = upper_pipe.x - 1
    if upper_pipe.right <= 0:
        upper_pipe.left = WIDTH
        flappy.score += 1
        print(flappy.score)

    # collision detection
    if flappy.colliderect(upper_pipe):
        print('Ta hlavou trubku neporazis.')
        quit()

    # head
    if flappy.top <= 0 or flappy.bottom >= HEIGHT:
        print('Z tohto sveta neutečieš.')
        quit()

def draw():
    screen.blit('background', (0, 0))
    upper_pipe.draw()
    flappy.draw()

def on_key_down():
    flappy.ay = -6.5