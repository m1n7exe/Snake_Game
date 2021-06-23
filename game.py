#python snake game
#by Min_P_Thar
#Modules
import turtle

import time

import random

delay = 0.1


#set up the screen

graphics = turtle.Screen()
graphics.title("Snake Game by Min")
graphics.bgcolor("black")
graphics.setup(width=600, height=600)
graphics.tracer(0) #turns off the screen update

#Create Sprite 1
head = turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("white")
head.penup()
head.pensize()
head.goto(x=0,y=0)
head.direction = "stop"


#Create Sprite 2
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("white")
food.turtlesize(0.7)
food.penup()
food.pensize()
food.goto(x=0,y=0)
food.direction = "stop"

#Create list

segments = []        #list

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0 ", align = "center" ,font=("Courier" ,24,"normal"))


#Functions

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
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)



#keyboard bindings

graphics.listen()
graphics.onkeypress(go_up, "w" )
graphics.onkeypress(go_down, "s" )
graphics.onkeypress(go_left, "a" )
graphics.onkeypress(go_right, "d" )
#Main game loop
while True:
    graphics.update() #Update graphics every time




    #Collision with Borders
    if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
        time.sleep(delay)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
         segment.goto(1000, 1000)

        #clear segments
        segments.clear()





    #Collision with food

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)


        #List
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #move the segments in reverse order
    for index in range(len(segments)-1,0,-1): #in the range of 1 to 9 #need to understand this line of code
        x = segments[index - 1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x,y)

        #move segment 0 to where the head is
    if len(segments) > 0:                    #in the range of 0/ only 0
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)




    move()
    time.sleep(delay)

    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

                segment.clear()







graphics.mainloop














