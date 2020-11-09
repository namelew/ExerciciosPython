import turtle as tt
ts = tt.getscreen()
t = tt.Turtle()
t.right(90) #turn the head 90 degree
t.forward(100) # move turtle 100 pixels ahead
t.right(90*3)    #                                               ^
t.forward(100)    #                                               |
t.left(90)        #                                        -x,+y  |  +x,+y
t.forward(100)    #                                        <------|------->
t.left(90)        #                                        -x,-y  |  +x,-y
t.forward(100)    #                                               |
#t.goto(x,y) # moves to x,y position in the quadrant            v
t.goto(0, 0) # center
t.home() # home position
t.circle(90) # radius / raio
#t.dot(diameter)
t.pensize(5) # thickness
t.penup() # move without trace
t.pendown() # trace again
t.undo()
t.clear() # clear screen
t.reset() # clear and restore the original values
nt = t.clone()
t.circle(50)
nt.color('blue')
nt.circle(100)
#tt.Terminator()
#ts.bye()
#ts=tt.getscreen()
nt.clear()
t.reset()
t.clear()
#nt.reset()
#nt.clear()
t = tt.Turtle()
for i in range(5, 51, 5):
    t.circle(i)
