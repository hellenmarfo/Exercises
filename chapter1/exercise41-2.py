#import turtle
#import math

#bob = turtle.Turtle()
#bob.speed(0)

#def arc(t, r, angle):
    #n = int(100 * angle / 360)
    #step_length = 2 * math.pi * r * angle / 360 / n
    #step_angle = angle / n

    #for i in range(n):
        #t.forward(step_length)
        #t.left(step_angle)

#def petal(t, r, angle):
    #for i in range(2):
        #arc(t, r, angle)
        #t.left(180 - angle)

#def flower(t, petals, r, angle):
    #for i in range(petals):
        #petal(t, r, angle)
        #t.left(360 / petals)

#flower(bob, 7, 80, 60)

#turtle.done()