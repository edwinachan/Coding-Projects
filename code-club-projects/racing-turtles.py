#https://codeclubprojects.org/en-GB/python/turtle-race/#

from turtle import *
from random import randint

#Start drawing from the top left corner

speed(10)
penup()
goto(-140,140)



#Create vertical tracks numbered 0-5. Use write function to achieve this
#right(90) makes the turtle turn right 90 degrees
#forward(10) moves the turtle by 10 units to create a gap between the track and the number
#Use pendown() to start drawing
#Use a loop to iterate through to 5
#We use range(6) as Python is zero-based

for i in range(15):
    write(i, align = 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
#Lift the pen up and go back up towards the length of the line plus the gap    
    penup()
    backward(160)
    left(90)
    forward(20)

#Create several racing turtles
#Make them move a random number of steps per go
#Winning turtle is the one that gets furthest in 100 turns

#Create a turtle ada
ada = Turtle()
ada.color('red')
ada.shape('turtle')

#Send ada to the starting line
ada.penup()
ada.goto(-160,100)
ada.pendown()

#Create another turtle named bob

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

#Make ada and bob move forward 1, 2, 3, 4 or 5 steps at each turn
#We use randint to choose a random number between 1 and 5
#Run through loop 100 times; make ada go 100 times

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))





