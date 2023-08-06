from random import randint
from time import time

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
number_of_dots = 3
next_dot = 0
game_over = False
start_time = 0

def next_level():
    global dots, lines, next_dot, number_of_dots, start_time
    dots = []
    lines = []
    next_dot = 0
    for dot in range(0, number_of_dots):
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), \
            randint(20, HEIGHT -20)
        dots.append(actor)
    start_time = time()

def draw():
    if game_over == True:
        screen.fill("pink")
        screen.draw.text("GameOver", center=(200, 200), fontsize = 60, color="#802020")
        return
    screen.fill("black")
    # screen.draw.text(str(round((time()-start_time)/60, 1)), topleft=(10, 10), fontsize = 16, color="#FFFFFF")
    screen.draw.text(str(round(time()-start_time, 1)), topleft=(10, 10), fontsize = 16, color="#FFFFFF")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), \
          (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

def update():
    pass
    # 今回のこの関数はfpsを60に固定するためだけの物

def on_mouse_down(pos):
    global number_of_dots
    global next_dot
    global lines
    global game_over
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))
        next_dot += 1
        if next_dot == number_of_dots:
            number_of_dots += 2
            next_level()
    else:
        game_over = True
        # lines = []
        # next_dot = 0

next_level()