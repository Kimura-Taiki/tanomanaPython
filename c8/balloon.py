from random import randint
# import pygame

WIDTH = 800
HEIGHT = 600

class Enemy(Actor):
    def __init__(self, image, top_y, bottom_y):
        super().__init__(image=image)
        self.top_y = top_y
        self.bottom_y = bottom_y
        self.repos()
    
    def hitten(self):
        global balloon
        if balloon.collidepoint(self.x, self.y) == False:
            return
        self.repos()
        damaged_ballon()

    def repos(self):
        self.pos = randint(800, 1600), randint(self.top_y, self.bottom_y)

balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Enemy("bird-up", 10, 200)

house = Actor("house")
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450


bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

lives = 3
hearts = []
for i in range(0,lives):
    heart = Actor("mini_heart")
    heart.pos = i*64+32, 24
    hearts.append(heart)

print("Heartsは")
print(hearts)

scores = []

def update_high_scores():
    global score, scores
    filename = r"/Users/kimurafutoshiki/Desktop/Python集/たのまなPython図鑑/c8/high-scores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
    for high_score in high_scores:
        if (score > int(high_score)):
            scores.append(str(score) + " ")
            score = int(high_score)
        else:
            scores.append(str(high_score) + " ")
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
        bird.draw()
        house.draw()
        tree.draw()
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

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1

    if bird.x > 0:
        bird.x -= 4
        if number_of_updates == 9:
            flap()
            number_of_updates = 0
        else:
            number_of_updates += 1
    else:
        bird.x = randint(800, 1600)
        bird.y = randint(10, 200)
        score += 1
        number_of_updates = 0

    if house.right > 0:
        house.x -= 2
    else:
        house.x = randint(800, 1600)
        score += 1

    if tree.right > 0:
        tree.x -= 2
    else:
        tree.x = randint(800, 1600)
        score += 1

    if balloon.top < 0 or balloon.bottom > 560:
        game_over = True
        update_high_scores()

    if balloon.collidepoint(house.x, house.y) or \
       balloon.collidepoint(tree.x, tree.y):
        game_over = True
        update_high_scores()

    bird.hitten()

def damaged_ballon(damage=1):
    global lives, game_over
    for i in range(lives - damage, lives):
        if i < 0:
            break
        del hearts[i]
    lives -= damage
    if lives <= 0:
        game_over = True
        update_high_scores()

