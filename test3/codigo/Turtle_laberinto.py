import turtle as t
import random as rd
from numpy import *

def SetBox():
    walls.hideturtle()
    walls.penup()
    walls.goto(-SetX_box,-SetY_box)
    walls.pendown()
    walls.goto(SetX_box,-SetY_box)
    walls.goto(SetX_box,SetY_box)
    walls.goto(-SetX_box,SetY_box)
    walls.goto(-SetX_box,-SetY_box)
    walls.penup()

def SetWall(number):
    #Levantar el pen, y esconder a la tortuga  
    walls.hideturtle()
    x_array = linspace(-SetX + 50 ,SetX - 50, number + 2)
    
    for i in range(number):
        walls.penup()
        x_cord = x_array[i+1]
        if(rd.random() > 0.5):
            y_cord = -SetY_box 
            y_fin = SetY_box - 30
        else:
            y_cord = SetY_box 
            y_fin = -SetY_box + 30 
        
        walls.goto(x_cord,y_cord)
        walls.pendown()
        walls.goto(x_cord,y_fin)
        
        
t.setup (width=1080, height=800, startx=0, starty=0)


walls = t.Turtle()
player = t.Turtle()
player.hideturtle()

screen_width = t.window_width()
screen_height = t.window_height()

PENSIZE = 5

print(screen_width)
print(screen_height)

SetX = -screen_width/2
SetY = -screen_height/2

SetX_box = -SetX - 20
SetY_box = -SetY - 30





#Acomodar la tortuga hacia arriba
walls.pensize(PENSIZE)
SetBox()
# walls
# walls.rt(270)
SetWall(3)

#EMPEZAR LO DE LA LINEA

# t.pensize(PENSIZE)
player.penup()
player.goto(-SetX_box + 5 ,-SetY_box + 5)
player.shape("turtle")
player.showturtle()

while player.xcor() < -SetX:
    # print("Distancia = " + str(player.distance(walls)))
    if(player.distance(walls) < 3):
        player.rd(90)
    else:
        player.fd(1)

t.exitonclick()