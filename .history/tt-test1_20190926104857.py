import turtle,time,random

tt=turtle.Turtle()
turtle.screensize(100,300)

def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.forward(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

duobianxing(4,200)

turtle.exitonclick()