from random import randint
import time

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

game_over = False
finalised = False
garden_happy = True
fangflower_collision = False

time_elapsed = 0
start_time = time.time()

cow = Actor("cow")
cow.pos = 100, 500
flower_list = []
wilted_list = []
fangflower_list = []
fangflower_vx_list = []
fangflower_vy_list = []

def draw():
    global game_over, time_elapsed, finalised
    if not game_over:
        screen.clear()
        screen.blit("garden", (0, 0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        for fangflower in fangflower_list:
            fangflower.draw()
        time_elapsed = int(time.time() - start_time)
        screen.draw.text(
            "Garden happy for: " +
            str(time_elapsed) + " seconds",
            topleft=(10, 10), color="black"
        )