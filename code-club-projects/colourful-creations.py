#https://codeclubprojects.org/en-GB/python/colourful-creations/

from turtle import *

#Set the screen up. 400x400 pixels with  background colour of white
#Use hex code from http://jumpto.cc/colour-picker

screen = Screen()
screen.setup(400,400)

#Create a dictionary to map from human-friendly colour names (keys) to
#computer-friendly hex codes (values)
#A colon separates the key (colour name) from the value (hex)

colours = {
    'reallyraspberry': '#F64ACB',
    'verylime': '#58D52E',
    'zestyorange': '#F8982A',
    'extremelyblue': '#2A79F8'
}


#If I wanted to print the hex code of a colour in my dictionary:
#print(colours['verylime'])

#Use the dictionay you just created to colour the background and text

screen.bgcolor(colours['verylime'])

#Write some text
penup()
goto(0,100)
color(colours['extremelyblue'])
style = ('Arial', 40, 'bold')
write('Hello', font = style, align = 'center')
right(90)
forward(60)
color(colours['reallyraspberry'])
write('World', font = style, align = 'center')
hideturtle()


