from turtle import *
from random import randint


speed(10)
penup()
goto(-140, 140)

for step in range(10):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(10)


turtleRed = Turtle()
turtleRed.color('red')
turtleRed.shape('turtle')

turtleRed.penup()
turtleRed.goto(-160, 100)
turtleRed.pendown()



turtleBlue = Turtle()
turtleBlue.color('blue')


turtleBlue.penup()
turtleBlue.goto(-160, 70)
turtleBlue.pendown()


for turn in range(50):
  # turtleBlue.forward(randint(1,3))
  turtleRed.forward(randint(1, 3))

done()