from random import randint

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

move_list = []
display_list = []

score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start")
dancer.pos = CENTRE_X + 5, CENTRE_Y - 40

up = Actor("up")
up.pos = CENTRE_X, CENTRE_Y + 100
right = Actor("right")
right.pos = CENTRE_X + 60, CENTRE_Y + 170
down = Actor("down")
down.pos = CENTRE_X, CENTRE_Y + 230
left = Actor("left")
left.pos = CENTRE_X - 60, CENTRE_Y + 170

def draw():
    global game_over, score, say_dance
    global count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " +
                         str(score), color="black",
                         topleft=(10, 10))
    return