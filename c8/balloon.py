from random import randint
# import pygame

WIDTH = 800
HEIGHT = 600

class Enemy(Actor):
    def __init__(self, image, top_y, bottom_y=-1, damage=1, shift_x=0):
        super().__init__(image=image)
        self.top_y = top_y
        if bottom_y == -1:
            self.bottom_y = self.top_y
        else:
            self.bottom_y = bottom_y
        self.damage = damage
        self.repos()
        self.x += shift_x
    
    def hitten(self,damage=1):
        global balloon
        if balloon.collidepoint(self.x, self.y) == False:
            return
        self.repos()
        damaged_ballon(self.damage)

    def repos(self):
        self.pos = randint(800, 1600), randint(self.top_y, self.bottom_y)
        self.avoided = False

    def appear_shift(self, x):
        self.x += x

    def move(self):
        global score
        if self.right < 0:
            self.repos()
        else:
            self.move_detail()
        if (self.avoided == False) and (self.right < 400):
            score += 1
            self.avoided = True
    
    def move_detail(self):
        self.x -= Enemy.speed(2)

    def speed(default):
        return int(default * (int(score / 5) + 4) / 4)

class EnemyBird(Enemy):
    def __init__(self, image, top_y, bottom_y=-1, damage=1, shift_x=0):
        super().__init__(image, top_y, bottom_y, damage, shift_x)
        self.number_of_updates = 0
        self.bird_up = True
    
    def move_detail(self):
        self.x -= Enemy.speed(4)
        if self.number_of_updates == 9:
            self.flap()
            self.number_of_updates = 0
        else:
            self.number_of_updates += 1
    
    def flap(self):
        if self.bird_up:
            self.image = "bird-down"
            self.bird_up = False
        else:
            self.image = "bird-up"
            self.bird_up = True



balloon = Actor("balloon")
balloon.pos = 400, 300

enemies = []
enemies.append(EnemyBird("bird-up", 10, 200))
enemies.append(EnemyBird("bird-up", 10, 200, shift_x=400))
enemies.append(Enemy("house", 460, damage=2))
enemies.append(Enemy("house", 460, damage=2, shift_x=400))
enemies.append(Enemy("tree", 450))
enemies.append(Enemy("tree", 450, shift_x=400))

up = False
game_over = False
score = 0

lives = 3
hearts = []
for i in range(0,lives):
    heart = Actor("mini_heart")
    heart.pos = i*64+32, 24
    hearts.append(heart)

scores = []

def update_high_scores():
    global score, scores
    new_high_score = False
    filename = r"/Users/kimurafutoshiki/Desktop/Python集/たのまなPython図鑑/c8/high-scores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
    for high_score in high_scores:
        if (score > int(high_score)):
            scores.append(str(score) + " ")
            score = int(high_score)
            new_high_score = True
        else:
            scores.append(str(high_score) + " ")
    if new_high_score == False:
        return
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high_score)

def display_high_socres():
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
        y += 25
        position += 1

def draw():
    global lives
    screen.blit("background", (0, 0))
    if not game_over:
        for heart in hearts:
            heart.draw()
        balloon.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        display_high_socres()

def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1
    
    if balloon.top < 0 or balloon.bottom > 560:
        damaged_ballon(damage=99)

    for enemy in enemies:
        enemy.move()
        enemy.hitten()

def damaged_ballon(damage=1):
    global lives, game_over
    for i in reversed(range(lives - damage, lives)):
        if i < 0:
            break
        del hearts[i]
    lives -= damage
    if lives <= 0:
        game_over = True
        update_high_scores()

