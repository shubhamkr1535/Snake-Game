# A classic Snake Game built using Python and Turtle graphics.


import turtle
import random
import time

# Game Configuration
delay = 0.1
score = 0
high_score = 0
snake_body = []

# Setup Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Improves performance

# Draw screen border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("black")
border.pensize(3)
border.penup()
border.goto(-300, 300)  # top-left corner
border.pendown()
for _ in range(10):
    if _ % 2 == 0:
        border.forward(600)  # width
        border.right(90)
    else:
        border.forward(600)  # height
        border.right(90)

# Create Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.fillcolor("blue")
food.penup()
food.goto(150, 250)

# Create Scoreboard
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-290, 260)
scoreboard.color("black")
scoreboard.write("Score: 0  High Score: 0", font=("Arial", 14, "normal"))

# Movement Functions
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_stop():
    head.direction = "stop"

def move():
    x, y = head.xcor(), head.ycor()
    if head.direction == "up":
        head.sety(y + 20)
    elif head.direction == "down":
        head.sety(y - 20)
    elif head.direction == "left":
        head.setx(x - 20)
    elif head.direction == "right":
        head.setx(x + 20)

# Keyboard Bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_stop, "space")

# Main Game Loop
while True:
    screen.update()

    # Border Wrapping
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Collision with food
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        snake_body.append(new_segment)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write(f"Score: {score}  High Score: {high_score}", font=("Arial", 14, "normal"))

        # Speed up
        delay = max(0.05, delay - 0.001)

    # Move body segments
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    if len(snake_body) > 0:
        snake_body[0].goto(head.xcor(), head.ycor())

    move()

    # Collision with self
    for segment in snake_body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide and reset snake body
            for segment in snake_body:
                segment.hideturtle()
                segment.goto(1000, 1000)
            snake_body.clear()

            # Reset score
            score = 0
            delay = 0.1
            scoreboard.clear()
            scoreboard.write(f"Score: {score}  High Score: {high_score}", font=("Arial", 14, "normal"))

    time.sleep(delay)

screen.mainloop()
