import turtle,time,random

turtle.screensize(100,100,"green")
tt=turtle.Turtle()

def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.forward(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

duobianxing(4,200)

turtle.exitonclick()