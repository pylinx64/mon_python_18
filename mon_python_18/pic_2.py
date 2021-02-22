import turtle
import time

t=turtle.Pen()
#----------------
turtle.bgcolor('black')

t.pencolor('#37FF0C')
t.forward(100)
t.left(100)
t.pencolor('#0CFCFF')
t.circle(100)


t.write('Alex', font=('Arial', 24))
t.penup()
t.forward(100)
t.pendown()
t.write('Alex', font=('Arial', 24))

#------------------
time.sleep(100)
