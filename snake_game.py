# PYTHON SNAKE GAME 

# Import Statement
import turtle
import time
import random

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Sangeetha Navaladi")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# snake body
segments = []

# score
score = 0
high_score = 0

# scoring funciton
scoring = turtle.Turtle()
scoring.color("white")
scoring.goto(1, 260)
scoring.penup()
scoring.speed(0)
scoring.hideturtle()
scoring.write("Score: 0  High Score: 0", align="center", font=("italic", 24, "normal"))

# Funcitons
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
   
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)    

# scoring funciton
def update_score():
    scoring.clear()
    scoring.write(f"Score: {score}  High Score: {high_score}", align="center", font=("italic", 24, "normal"))

# keyboard binding
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# main game loop
while True:
    wn.update()
    
    # collision with the borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # clear the segments
        segments.clear()

        # Update score
        score = 0
        update_score()   


    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()
            # Update score
            score = 0
            update_score()        

    # collision of the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # snake body (add a segments)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 1
        if score > high_score:
            high_score = score
        update_score()    
    
    for index in range(len(segments)- 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()
    time.sleep(0.1)
