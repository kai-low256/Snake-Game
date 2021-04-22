# Importing
import random
import time
import turtle

delay = 0.1

# Score
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()    #* Opening the Turtle Screen
wn.title("Snake")  #* Naming the screen
wn.bgcolor("green")     #* Setting up background colour of the screen
wn.setup(width = 600, height = 600)     #* Setting up the size of the screen unless fullscreen
wn.tracer(0)    #* Stops Screen Animations

# Snake head
head = turtle.Turtle()  #* Defining the Varible as tutle
head.speed(0)   #* Adjusts the speed of the sake head when played (does not effect anything when removed)
head.shape("square")    #** Shape of the Head 
head.color("black") #* Colour of the Head
head.penup()    #* Stops snake head from making copies of itself
head.goto(0,0)   #* Head goes to point (0,0) when screen is open
head.direction = "stop"     #* Stops snake head from moving when screen is open

# Snake food
food = turtle.Turtle()  #* Defining the Varible as turtle
food.speed(0)   #* Adjusts the speed of the food when appear (does not effect anything when removed)
food.shape("circle")     #* Shape of the food
food.color("red")   #* Colour of the food
food.penup()    #* Stops snake food from making copies of itself
food.goto(0,100)    #* Prevents Food from spawning in the same position as snake head

#* Makes square segments so that snake square body does not over lap each other, food also spawns in its own segments (Like a grid)
segments = []

# Pen to write Score Text
pen = turtle.Turtle()   #* Defining the Varible as turtle
pen.speed(0)    #* Adjusts the speed of the Score text
pen.shape("square") #* Changes the shape of the text but its useless
pen.color("white")  #* Changes the colour of the text or else its going to be black
pen.penup() #* When Snake Moves, Does not change the text
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 Highest Score: 0", align = "center", font = ("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 22)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 22)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 22)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 22)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    #* Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        print("\nDead\n")

        #* Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #* Clear the segments list
        segments.clear()

        #* Reset the score
        score = 0

        #* Reset the delay
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  Highest Score: {high_score}", align = "center", font = ("Courier", 24, "normal"))


    #*Check for a collision with the food

    if head.distance(food)<20:
        #* move the food to a random spot
        x = random.randint(-285,285)
        y = random.randint(-285,285)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #* Shorten the delay
        delay -= 0.001

        #* Increase the score
        score += 1
        print(score)

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  Highest Score: {high_score}", align="center",font=("Courier", 24, "normal"))

    #* Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #* Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #* Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            print("\nDead\n")

            #* Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}  Highest Score: {high_score}", align = "center",font = ("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
