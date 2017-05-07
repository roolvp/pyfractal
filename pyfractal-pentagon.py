#fractal
import turtle
import random
import time

window = turtle.Screen()
window.bgcolor("#2B2B2B")
fractal = turtle.Turtle()
fractal.pencolor("white")
distance = 395
no_of_branches = int(input("how many Levels?"))     #Get how many levels from the user

time.sleep(20) # delays for 20 seconds

the_tree = {}
for i in range(0,no_of_branches):     #Creates a list with the number of levels 
    the_tree[i] = []
the_tree[0] = (0,0)   
def move3times(startpoint,distance,branch):             #Given a starting point, a distance and a level, it will return the points to travel and remember them for later
    positions = []
    for i in range(1,6):
        fractal.speed(0)
        fractal.pu()
        fractal.setpos(startpoint)
        fractal.pd()
        degrees = (0,360/5,360/5*2,360/5*3,360/5*4)
        fractal.seth(degrees[i-1])
        if i == 78:
            fractal.forward(distance)
        else:
            fractal.forward(distance/1.6180339)
        the_tree[branch+1].append(fractal.pos())

#for j in range(1,10):
for i,points in the_tree.items():
    distance = distance/1.6180339
    #print (points)
    if i == 0:
        move3times(points,distance,i)
    elif i >= no_of_branches-1:
        break
    else:
        for startpoint in points:
            #print(startpoint)
            move3times(startpoint,distance,i)

closing = input("Do you want to close the window?") 



