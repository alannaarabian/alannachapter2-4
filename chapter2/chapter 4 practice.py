import turtle
size=150
def makesqaure(turt,size):
    print(size)
    for i in range (4):
        turt.forward(100)
        turt.left(90)

wn=turtle.Screen()
sachin=turtle.Turtle()
sachin.color("orange")

andy= turtle.Turtle()

andy.setpos(100,100)

makesqaure(andy)
makesqaure (sachin)
print(size)
