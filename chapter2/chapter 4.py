import turtle

def make_window(colr,ttle):
    """
    set up a turtle with the given clor and pensize
    returns the new turtle
    """
    t=turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def make_sqaure():
    for i in range (4):
        turt.pendown()
        ess.forward(20)
        ess.left(90)
        turt.penup()
        turt.forward(sz*20) 
    
wn= make_window("lightgreen", "sqaures")

ess=make_turtle("blue",5)

for i in range(4):
    make_sqaure

make_sqaure()