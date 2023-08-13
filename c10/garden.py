from random import randint
from pgzero import actor
import time

from pgzero.actor import ANCHOR_CENTER, POS_TOPLEFT

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

game_over = False
finalised = False
garden_happy = True
fangflower_collision = False

score = 0

time_elapsed = 0
start_time = time.time()

cow = Actor("cow")
cow.pos = 100, 500
flower_list = []
fangflower_list = []


class Flower(actor.Actor):
    def __init__(self, image):
        super().__init__(image=image)
        self.wilted_since = "happy"

class Fangflower(actor.Actor):
    def __init__(self, image):
        super().__init__(image=image)
        self.vx = 0
        self.vy = 0

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
    else:
        if not finalised:
            cow.draw()
            screen.draw.text(
                "Garden happy for: " +
                str(time_elapsed) + " seconds",
                topleft=(10, 10), color="black"
            )
            if (not garden_happy):
                screen.draw.text(
                    "GARDEN UNHAPPY - GAME OVER!", color="black",
                    topleft=(10, 50)
                )
                finalised = True
            else:
                screen.draw.text(
                    "FANGFLOWER ATTACK - GAME OVER!", color="black",
                    topleft=(10, 50)
                )
                finalised = True
    return

def new_flowers():
    global flower_list
    flower_new = Flower("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    flower_new.wilted_since = "happy"
    flower_list.append(flower_new)
    return

def add_flowers():
    global game_over
    if not game_over:
        new_flowers()
        clock.schedule(add_flowers, 4)
    return

def check_wilt_times():
    global game_over, garden_happy, flower_list
    for flower in flower_list:
        if flower.wilted_since == "happy":
            continue
        if int(time.time() - flower.wilted_since) > 10.0:
            garden_happy = False
            game_over = True
            break
    return

def wilt_flower():
    global flower_list, game_over
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list) - 1)
            if (flower_list[rand_flower].image == "flower"):
                flower_list[rand_flower].image = "flower-wilt"
                flower_list[rand_flower].wilted_since = time.time()
        clock.schedule(wilt_flower, 3)
    return

def check_flower_collision():
    global cow, flower_list
    index = 0
    for flower in flower_list:
        if (flower.colliderect(cow) and
            flower.image == "flower-wilt"):
            flower.image = "flower"
            flower.wilted_since = "happy"
            break
        index += 1
    return

def check_fangflower_collision():
    global cow, fangflower_list, fangflower_collision
    global game_over
    for fangflower in fangflower_list:
        if fangflower.colliderect(cow):
            cow.image = "zap"
            game_over = True
            break
    return

def velocity():
    random_dir = randint(0, 1)
    random_velocity = randint(2, 3)
    if random_dir == 0:
        return -random_velocity
    else:
        return random_velocity

def mutate():
    global flower_list, fangflower_list, game_over
    if not game_over and flower_list:
        rand_flower = randint(0, len(flower_list) - 1)
        fangflower = Fangflower("fangflower")
        fangflower.pos = flower_list[rand_flower].x, flower_list[rand_flower].y
        fangflower.vx = velocity()
        fangflower.vy = velocity()
        clock.schedule(mutate, 20)
        fangflower = fangflower_list.append(fangflower)
        del flower_list[rand_flower]
    return

def update_fangflowers():
    global fangflower_list, game_over
    if not game_over:
        index = 0
        for fangflower in fangflower_list:
            fangflower.x += fangflower.vx
            fangflower.y += fangflower.vy
            if (fangflower.left < 0) or (fangflower.right > WIDTH):
                fangflower.vx *= -1
            if (fangflower.top < 150) or (fangflower.bottom > HEIGHT):
                fangflower.vy *= -1
            index += 1
    return

def reset_cow():
    global game_over
    if not game_over:
        cow.image = "cow"
    return

def update():
    global score, game_over, fangflower_collision
    global flower_list, fangflower_list, time_elapsed
    fangflower_collision = check_fangflower_collision()
    check_wilt_times()
    if not game_over:
        if keyboard.space:
            cow.image = "cow-water"
            clock.schedule(reset_cow, 0.5)
            check_flower_collision()
        if keyboard.left and cow.x > 0:
            cow.x -= 5
        elif keyboard.right and cow.x < WIDTH:
            cow.x += 5
        if keyboard.up and cow.y > 0:
            cow.y -= 5
        elif keyboard.down and cow.y < HEIGHT:
            cow.y += 5
        update_fangflowers()

def start_mutate():
    clock.schedule(mutate, 5)

add_flowers()
wilt_flower()
start_mutate()