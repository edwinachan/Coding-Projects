#https://codeclubprojects.org/en-GB/python/colourful-creations/
#Creating my own poster that declares my love for ramen

from turtle import *

#Set up a screen that is 400x400 pixels big

screen = Screen()
screen.setup(800, 800)

#Create a dictionary to map from human-friendly colour names (keys) to
#computer-friendly hex codes (values)
#A colon separates the key (colour name) from the value (hex)

colours = {
    'pastelpink': '#DD9391',
    'whitehot': '#FFFFFF',
    'noodles': '#ECDA63',
    'teastainedegg': '#B8A219',
    'freshgreens': '#6AB03F',
    'eggyolk': '#F5AC0F'
}

screen.bgcolor(colours['pastelpink'])

#Create a red circle to put your text in
speed(1)
color(colours['whitehot'])
dot(600)
penup()
goto(0,100)
color(colours['noodles'])
style = ('Arial', 100, 'bold')
write('Ed', font = style, align = 'center')
right(90)
forward(100)
color(colours['freshgreens'])
write('Really', font = style, align = 'center')
forward(100)
color(colours['teastainedegg'])
write('Loves', font = style, align = 'center')
forward(100)
color(colours['eggyolk'])
write('Ramen', font = style, align = 'center')
hideturtle()
