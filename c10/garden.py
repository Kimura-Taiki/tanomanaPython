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

score = 0

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
    else:
        if not finalised:
            cow.draw()
            screen.draw.text(
                "GARDEN UNHAPPY - GAME OVER!", color="black",
                topleft=(10, 50)
            )
            finalised = True

def new_flowers():
    global flower_list, wilted_list
    flower_new = Actor("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    flower_list.append(flower_new)
    wilted_list.append("happy")
    return

def add_flowers():
    global game_over
    if not game_over:
        new_flowers()
        clock.schedule(add_flowers, 4)
    return

def check_wilt_times():
    global wilted_list, game_over, garden_happy
    if wilted_list:
        for wilted_since in wilted_list:
            if (not wilted_since == "happy"):
                time_wilted = int(time.time() - wilted_since)
                if (time_wilted) > 10.0:
                    garden_happy = False
                    game_over = True
                    break
    return

def wilt_flower():
    global flower_list, wilted_list, game_over
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list) - 1)
            if (flower_list[rand_flower].image == "flower"):
                flower_list[rand_flower].image = "flower-wilt"
                wilted_list[rand_flower] = time.time()
        clock.schedule(wilt_flower, 3)
    return

def check_flower_collision():
    global cow, flower_list, wilted_list
    index = 0
    for flower in flower_list:
        if (flower.colliderect(cow) and
            flower.image == "flower-wilt"):
            flower.image = "flower"
            wilted_list[index] = "happy"
            break
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

add_flowers()
wilt_flower()