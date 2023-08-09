WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
time_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
time_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["What is the capital of France?", "London", "Paris", "Berlin", "Tokyo", 2]
q2 = ["What is 5+7?", "12", "10", "14", "8", 1]
q3 = ["What is the seventh month of the year?", "April", "May", "June", "July", 4]
q4 = ["Which planet is closest to the Sun?", "Saturn", "Neptune", "Mercury", "Venus", 3]
q5 = ["Where are the pyramids?", "India", "Egypt", "Morocco", "Canada", 2]
questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(time_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
    
    screen.draw.textbox(str(time_left), time_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index += 1

def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass