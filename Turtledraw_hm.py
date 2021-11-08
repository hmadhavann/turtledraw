# TurtleDraw
#
# By: Hima Madhavan
#
# All Rights Reserved

import turtle
import math

print('Welcome to Turtle Draw!')
TEXTFILENAME = input('Please Enter the File Name:\n')
TEXTFILENAME = 'turtledraw.txt'
print('Here We Go!')

sc = turtle.Screen()
sc.setup(450,450)

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()

turtledrawTextFile = open(TEXTFILENAME, 'r')
line = turtledrawTextFile.readline()

while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) ==3):
            color = parts[0]
            x = int(parts[1])
            y = int(parts[2])

            turtleDraw.color(color)
            turtleDraw.goto(x,y)
        
            previousposition = [0,0]
            currentPosition = [x,y]
           
            turtledistance = []
            turtledistance = [math.sqrt( ((currentPosition[0]-previousposition[0])**2)+((currentPosition[1]-previousposition[1])**2) )]
            totaldistance = [sum(turtledistance)]
            previousposition = currentPosition
           
            totaldistance = [sum(turtledistance)]
            finaltotaldistance = [sum(totaldistance)]
            print('')
            print(totaldistance)
            
    style = ('courier', 60, 'italic')
    turtle.speed(10)
    turtle.write('total distance=' + str(finaltotaldistance), align= 'left', move= 'false')
          
    turtleDraw.pendown()

    if (len(parts) ==1): 
     turtleDraw.penup()

    line = turtledrawTextFile.readline()

turtle.Screen().exitonclick()
turtledrawTextFile.close()



print('\nEnd')