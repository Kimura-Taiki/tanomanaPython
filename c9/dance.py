from random import randint

# from enum import Enum

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

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

# 1. 最初のgenerate_movesでshow_countdownはTrue、say_danceはFalseとされる。
#   show_countdown中はcountdownが定期発動する。
show_countdown = True
# 2. countdownが終わると、show_countdownはFalseとされ、say_danceも引き続きFalseとされる。
#   と同時にdisplay_movesが起動して以降はdisplay_movesが定期発動する。
say_dance = False
# 3. display_movesが終わると、say_danceはTrueとされる。
#   on_key_upでnext_moveを起動していく。
moves_complete = False
# 4. next_moveが終わると、moves_completeはTrueとされる。
#   updateがこのTrueを拾って再びgenerate_moveが呼び出されゲームは繰り返す。
game_over = False
# 5. on_key_upで失敗すると、game_overはTrueとされる。
#   game_overはdrawの分岐を大きくずらすので原則ここでおしまい。
dancer = Actor("dancer-start")
dancer.pos = CENTRE_X + 5, CENTRE_Y - 40

class Button(Actor):
    def __init__(self, btn, x, y, key):
        super().__init__(image=btn)
        self.btn = btn
        self.pos = CENTRE_X + x, CENTRE_Y + y
        self.key = key
    
    def light_up(self):
        global dancer
        self.image = self.btn + "-lit"
        dancer.image = "dancer-" + self.btn
        clock.schedule(reset_dancer, 0.5)

up =    Button(btn="up",    x=0,    y=100,  key=keys.UP)
right = Button(btn="right", x=60,   y=170,  key=keys.RIGHT)
down =  Button(btn="down",  x=0,    y=230,  key=keys.DOWN)
left =  Button(btn="left",  x=-60,  y=170,  key=keys.LEFT)
enter = Button(btn="enter", x=0,    y=170,  key=keys.RETURN)
buttons = [up, right, down, left, enter]

def draw():
    global game_over, score, say_dance
    global count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        for button in buttons:
            button.draw()
        screen.draw.text("Score: " +
                         str(score), color="black",
                         topleft=(10, 10))
        if say_dance:
            screen.draw.text("Dance!", color="black",
                            topleft=(CENTRE_X - 65, 150), fontsize=60)
        if show_countdown:
            screen.draw.text(str(count), color="black",
                            topleft=(CENTRE_X - 8, 150), fontsize=60)
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Score: " +
                         str(score), color="black",
                         topleft=(10, 10))
        screen.draw.text("GAME OVER!", color="black",
                         topleft=(CENTRE_X - 130, 220), fontsize=60)
    return

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        for button in buttons:
            button.image = button.btn
    return

def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        for i, button in enumerate(buttons):
            if this_move != i:
                continue
            button.light_up()
            clock.schedule(display_moves, 1)
            break
    else:
        say_dance = True
        show_countdown = False
    return

def generate_moves():
    global move_list, dance_length, count
    global show_countdown, say_dance, buttons
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        rand_move = randint(0, len(buttons) - 1)
        move_list.append(rand_move)
        display_list.append(rand_move)
    show_countdown = True
    countdown()
    return

def countdown():
    global count, game_over, show_countdown
    if count > 1:
        count -= 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False
        display_moves()
    return

def next_move():
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move += 1
    else:
        moves_complete = True
    return

def on_key_up(key):
    global score, game_over, move_list, current_move
    for i, button in enumerate(buttons):
        if key != button.key:
            continue
        button.light_up()
        if move_list[current_move] == i:
            score += 1
            next_move()
            break
        else:
            game_over = True
    return

def update():
    global game_over, current_move, moves_complete
    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        music.stop()

generate_moves()
music.play("vanishing-horizon")