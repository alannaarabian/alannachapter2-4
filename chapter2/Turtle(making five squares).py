import turtle

wn=turtle.Screen()
owen=turtle.Turtle()

pendown()
def make_squares(turt,size,num):
    for i in range(4):
        turt.forward(size)
        turt.left(90)
        turt.left(90)
        
        
        turt.penup()
        turt.forward(2*size)
        make_square(owen,20)